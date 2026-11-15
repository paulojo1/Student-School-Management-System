# Student Result Management System

A simple menu-driven Python program to manage student records and results.

## Features
- Add, view, search, update and delete students
- Record scores for 5 subjects, with automatic total, average and grade
- Report card for each student
- Results list sorted by average or name
- Class statistics (highest, lowest, class average)
- Save a text report to `reports/class_report.txt`
- Data saved in `data/students.json` and loaded when the program starts

## How to run
Requires Python 3 only (no extra packages).

```
python main.py
```

## Files
- `main.py` - menu and program flow
- `student.py` - the `Student` class
- `results.py` - totals, averages, grades, class statistics
- `storage.py` - loading and saving JSON
- `reports.py` - report card and text report

## Grading
70+ = A, 60-69 = B, 50-59 = C, 40-49 = D, below 40 = F

## Python concepts used
Variables and type conversion, if/elif/else, for and while loops, lists,
dictionaries, functions, sorting with `sorted`, exception handling
(`try/except/else/finally`), JSON file handling, multiple modules,
a class (`Student`), `datetime`, regular expressions, and the standard
library (`os`, `json`, `re`, `datetime`).
