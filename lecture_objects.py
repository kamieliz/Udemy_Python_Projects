# Custom Objects: Classes
# Everything in Python is an Object
# You can create your own custom objects
# Functions associated with instances of objects are known as methods
# we are going to create a student Class
class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
 # adding helpful methods to our student Class
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name,self.last_name,self.courses)
            with open(filename,"a+") as to_write:
                to_write.write(record_to_add+"\n")
            return "Record added"


    def find_in_file(self,filename):
        with open(file_name) as f:
            for line in f:
                print(line.strip())
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False
    def update_file(self,filename):
        pass
        
    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name,courses):
        full_name = first_name+','+last_name
        courses = ",".join(courses)
        return full_name+':'+courses

    def __eq__(self,other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

# How you would like your object to be instantiated
    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name}','{self.courses}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
        \nCourses: {', '.join(map(str.capitalize, self.courses))}"

courses_1 = ['python','rails','javascript']
courses_2 = ['java', 'rails','c']
mashrur = Student("mashrur","hossain",courses_1)
john = Student("john","doe",courses_2)
file_name = "data.txt"
# print(mashrur)
# print(john)
print(mashrur.find_in_file(file_name))
print(mashrur.add_to_file(file_name))
joe = Student("joe","schmo",["python","ruby","javascript"])
print(joe.find_in_file(file_name))
print(joe.add_to_file(file_name))


# print(mashrur.first_name, mashrur.last_name, mashrur.courses)
# print(john.first_name, john.last_name, john.courses)
# mashrur.add_course("java")
# mashrur.add_course("rails")
# print(mashrur.first_name, mashrur.last_name, mashrur.courses)
# john.remove_course("c")
# john.remove_course("c")
# john.remove_course("python")
# print(john.first_name, john.last_name, john.courses)
