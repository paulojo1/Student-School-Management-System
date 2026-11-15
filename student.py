"""The Student class."""


class Student:
    def __init__(self, student_id, name, student_class, gender, dob,
                 scores=None, date_entered=""):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores is not None else {}
        self.date_entered = date_entered

    def to_dict(self):
        """Turn the student into a dictionary so it can be saved as JSON."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "student_class": self.student_class,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "date_entered": self.date_entered,
        }
