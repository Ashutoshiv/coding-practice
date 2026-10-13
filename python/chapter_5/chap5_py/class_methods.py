# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represent the class itself.

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

#   INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count}"  

student1 = Student("Spongbob", 3.5)
student2 = Student("Sunny Kumar", 4)
student3 = Student("Ashutosh", 3)

print(Student.get_count())
print(Student.get_average_gpa())