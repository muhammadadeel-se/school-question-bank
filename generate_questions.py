import random
import pandas as pd

# Set seed for reproducible dataset generation
random.seed(42)

OPENERS = [
    "",
    "Hi, ",
    "Hello, ",
    "Quick question: ",
    "Could you please clarify, ",
]

SUBJECTS = [
    "my child",
    "my son",
    "my daughter",
    "new students",
]

TOPICS = [
    # --- Category: Fees (4 topics) ---
    {
        "topic": "Fee deadline",
        "category": "Fees",
        "expected_answer": "Monthly tuition fees are due by the 10th of each month.",
        "templates": [
            "{opener}when is the last date to pay the monthly tuition fee for {subject}?",
            "{opener}what is the official fee submission deadline each month for {subject}?",
            "{opener}by which date do I need to clear the school fees for {subject}?",
            "{opener}could you confirm the due date for this term's tuition fee for {subject}?",
        ],
    },
    {
        "topic": "Late fee penalty",
        "category": "Fees",
        "expected_answer": "A late payment surcharge of 5% is applied if fees are paid after the 10th of the month.",
        "templates": [
            "{opener}is there a late fee fine if I submit the tuition payment a few days late for {subject}?",
            "{opener}how much penalty is charged after the fee due date passes for {subject}?",
            "{opener}what happens if the monthly fee payment for {subject} is delayed past the deadline?",
            "{opener}do you charge a late payment surcharge on overdue school fees for {subject}?",
        ],
    },
    {
        "topic": "Sibling discount",
        "category": "Fees",
        "expected_answer": "Families with two or more enrolled children receive a 10% tuition discount for each additional sibling.",
        "templates": [
            "{opener}does the school offer any sibling discount on tuition fees for {subject}?",
            "{opener}how much fee concession is available if I enroll another sibling alongside {subject}?",
            "{opener}are there reduced tuition rates when multiple children from the same family attend with {subject}?",
            "{opener}how can I apply for a sibling fee discount for {subject}?",
        ],
    },
    {
        "topic": "Payment methods",
        "category": "Fees",
        "expected_answer": "Fees can be paid via online bank transfer, debit or credit card on the parent portal, or direct bank deposit.",
        "templates": [
            "{opener}what payment methods are accepted for paying school fees for {subject}?",
            "{opener}can I pay the tuition fee online using a debit card or bank transfer for {subject}?",
            "{opener}is there an online portal option to submit school fees for {subject}?",
            "{opener}do you accept direct bank deposits for the term fees of {subject}?",
        ],
    },
    # --- Category: Holidays (3 topics) ---
    {
        "topic": "Winter break",
        "category": "Holidays",
        "expected_answer": "Winter break runs from December 22 to January 5, and classes resume on January 6.",
        "templates": [
            "{opener}when does the winter break start and end this academic year for {subject}?",
            "{opener}what are the exact dates for the upcoming winter vacation for {subject}?",
            "{opener}which date do classes resume after the winter holidays for {subject}?",
            "{opener}how long is the school closed during winter break for {subject}?",
        ],
    },
    {
        "topic": "Summer vacation",
        "category": "Holidays",
        "expected_answer": "Summer vacation begins on June 15 and ends on August 14, with school reopening on August 15.",
        "templates": [
            "{opener}when do the summer holidays begin this year for {subject}?",
            "{opener}what is the reopening date after summer vacation for {subject}?",
            "{opener}can you share the summer break schedule for {subject}?",
            "{opener}how many weeks is the summer vacation period for {subject}?",
        ],
    },
    {
        "topic": "Public holidays",
        "category": "Holidays",
        "expected_answer": "The school closes on all national public holidays, and notices are posted on the parent portal two days prior.",
        "templates": [
            "{opener}does the school observe all national public holidays for {subject}?",
            "{opener}how are parents notified about upcoming public holiday closures for {subject}?",
            "{opener}will there be regular classes or a day off on gazetted public holidays for {subject}?",
            "{opener}where can I check the list of official public holidays for {subject}?",
        ],
    },
    # --- Category: Behavior Rules (3 topics) ---
    {
        "topic": "Uniform policy",
        "category": "Behavior Rules",
        "expected_answer": "Students must wear the regular school uniform and black shoes Monday through Thursday, and the sports kit on Fridays.",
        "templates": [
            "{opener}what is the mandatory daily school uniform code for {subject}?",
            "{opener}on which days should I send {subject} in the sports uniform instead of regular uniform?",
            "{opener}are black shoes strictly required as part of the uniform rules for {subject}?",
            "{opener}could you share the dress code and uniform guidelines for {subject}?",
        ],
    },
    {
        "topic": "Mobile phone policy",
        "category": "Behavior Rules",
        "expected_answer": "Mobile phones are not allowed during school hours; emergency devices must be turned off and handed in at the front office.",
        "templates": [
            "{opener}is it okay if {subject} brings a mobile phone to school for after-school pickup coordination?",
            "{opener}what is the school policy regarding smartphones and electronic devices for {subject}?",
            "{opener}where should emergency phones be deposited during class hours for {subject}?",
            "{opener}are mobile phones strictly banned inside classrooms for {subject}?",
        ],
    },
    {
        "topic": "Attendance and punctuality",
        "category": "Behavior Rules",
        "expected_answer": "Classes begin at 8:00 AM; arrivals after 8:10 AM are marked late, and at least 85% attendance is mandatory.",
        "templates": [
            "{opener}what time does the morning bell ring and when is late arrival marked for {subject}?",
            "{opener}what is the minimum attendance percentage required during the term for {subject}?",
            "{opener}what happens if {subject} arrives after 8:10 AM in the morning?",
            "{opener}could you explain the punctuality and attendance rules for {subject}?",
        ],
    },
]


def format_question(template: str, opener: str, subject: str) -> str:
    raw = template.format(opener=opener, subject=subject).strip()
    return raw[0].upper() + raw[1:]


def generate_dataset(questions_per_topic: int = 5) -> pd.DataFrame:
    records = []

    for item in TOPICS:
        # Generate all valid combinations for this topic
        combinations = [
            format_question(tmpl, opener, subj)
            for tmpl in item["templates"]
            for opener in OPENERS
            for subj in SUBJECTS
        ]
        # Ensure uniqueness and sample the required count per topic
        unique_combinations = sorted(set(combinations))
        sampled_questions = random.sample(unique_combinations, questions_per_topic)

        for q in sampled_questions:
            records.append(
                {
                    "Question": q,
                    "Expected Answer": item["expected_answer"],
                    "Category": item["category"],
                }
            )

    # Shuffle across categories and assign sequential IDs
    random.shuffle(records)
    df = pd.DataFrame(records)
    df.insert(0, "ID", range(1, len(df) + 1))

    # Validation checks before saving
    assert len(df) == 50, f"Expected 50 rows, got {len(df)}"
    assert df["Question"].nunique() == 50, "Duplicate questions detected!"
    assert list(df.columns) == ["ID", "Question", "Expected Answer", "Category"]

    return df


if __name__ == "__main__":
    dataset = generate_dataset(questions_per_topic=5)
    output_file = "school_question_bank.csv"
    dataset.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Successfully generated {len(dataset)} unique questions in '{output_file}'.")
    print("\nCategory breakdown:")
    print(dataset["Category"].value_counts().to_string())