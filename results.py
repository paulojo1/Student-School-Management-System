"""Score calculations and grading."""

SUBJECTS = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]


def get_total(scores):
    return sum(scores.values())


def get_average(scores):
    if len(scores) == 0:
        return 0
    return get_total(scores) / len(scores)


def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def class_stats(students):
    """Return (highest total, lowest total, class average) or None."""
    totals = []
    averages = []
    for s in students:
        if s.scores:
            totals.append(get_total(s.scores))
            averages.append(get_average(s.scores))
    if len(totals) == 0:
        return None
    return max(totals), min(totals), sum(averages) / len(averages)
