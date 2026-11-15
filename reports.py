"""Reports: report card, results table and saved text report."""
import os
from datetime import datetime

import results


def report_card(student):
    lines = []
    lines.append("=" * 40)
    lines.append("REPORT CARD")
    lines.append("=" * 40)
    lines.append(f"ID    : {student.student_id}")
    lines.append(f"Name  : {student.name}")
    lines.append(f"Class : {student.student_class}")
    lines.append("-" * 40)
    if len(student.scores) == 0:
        lines.append("No scores recorded yet.")
    else:
        for subject, score in student.scores.items():
            lines.append(f"{subject:<15}{score:>6.1f}")
        average = results.get_average(student.scores)
        lines.append("-" * 40)
        lines.append(f"Total   : {results.get_total(student.scores):.1f}")
        lines.append(f"Average : {average:.2f}")
        lines.append(f"Grade   : {results.get_grade(average)}")
        lines.append(f"Entered : {student.date_entered}")
    lines.append("=" * 40)
    return "\n".join(lines)


def results_table(students):
    lines = [f"{'ID':<10}{'Name':<22}{'Total':>8}{'Average':>9}{'Grade':>7}"]
    lines.append("-" * 56)
    for s in students:
        if s.scores:
            average = results.get_average(s.scores)
            lines.append(f"{s.student_id:<10}{s.name:<22}"
                         f"{results.get_total(s.scores):>8.1f}"
                         f"{average:>9.2f}{results.get_grade(average):>7}")
        else:
            lines.append(f"{s.student_id:<10}{s.name:<22}   (no scores)")
    return "\n".join(lines)


def save_report(students):
    """Save a text report to reports/class_report.txt and return the path."""
    ordered = sorted(students,
                     key=lambda s: results.get_average(s.scores),
                     reverse=True)
    text = "CLASS REPORT - " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n\n"
    text += results_table(ordered) + "\n"
    stats = results.class_stats(students)
    if stats is not None:
        highest, lowest, average = stats
        text += f"\nHighest total: {highest:.1f}"
        text += f"\nLowest total : {lowest:.1f}"
        text += f"\nClass average: {average:.2f}\n"

    os.makedirs("reports", exist_ok=True)
    path = os.path.join("reports", "class_report.txt")
    with open(path, "w") as file:
        file.write(text)
    return path
