class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
            enrolled in the {course} course")


class StudentAthlete(Student):

    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first,last,courses)
        self.sport = sport

courses = ["python","ruby","javascript"]
jane = StudentAthlete("jane","doe",courses, "hockey")
print(jane.sport)
print(isinstance(jane, StudentAthlete))
