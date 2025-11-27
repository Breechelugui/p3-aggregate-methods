class Course:
    all = []

    def __init__(self, name):
        self.name = name
        self._enrollments = []  # list of Enrollment instances
        Course.all.append(self)

    def add_enrollment(self, enrollment):
        from enrollment import Enrollment
        if not isinstance(enrollment, Enrollment):
            raise Exception("Must pass an Enrollment instance")
        self._enrollments.append(enrollment)

    def enrollment_count(self):
        return len(self._enrollments)
