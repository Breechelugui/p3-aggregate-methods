class Student:
    all = []

    def __init__(self, name):
        self.name = name
        self._enrollments = []  # list of Enrollment instances
        self._grades = {}       # optional: enrollment -> grade
        Student.all.append(self)

    def enroll(self, enrollment):
        from enrollment import Enrollment
        if not isinstance(enrollment, Enrollment):
            raise Exception("Must pass an Enrollment instance")
        self._enrollments.append(enrollment)

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:
            return 0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses
