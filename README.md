# School AI Question Bank (Synthetic Evaluation Dataset)

A Python-generated synthetic dataset of **50 unique parent queries** designed to benchmark and evaluate a school assistant AI across three core policy domains: **Fees**, **Holidays**, and **Behavior Rules**.

## Dataset Schema

The generated CSV (`school_question_bank.csv`) contains 50 rows with the following columns:

| Column | Description |
| :--- | :--- |
| `ID` | Sequential integer identifier (`1` to `50`) |
| `Question` | Natural-language parent query generated via parameterized templates |
| `Expected Answer` | Concise, factual ground-truth answer based on fictional school policy |
| `Category` | High-level domain (`Fees`, `Holidays`, or `Behavior Rules`) |

## Base Topics Covered (10 Topics)

- **Fees (20 questions):** Fee deadline, Late fee penalty, Sibling discount, Payment methods
- **Holidays (15 questions):** Winter break, Summer vacation, Public holidays
- **Behavior Rules (15 questions):** Uniform policy, Mobile phone policy, Attendance and punctuality

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt