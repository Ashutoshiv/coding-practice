# class variables = Shared among all instances of a class
                #   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 39)
student3 = Student("Sunny", 18)
student4 = Student("Yash", 25)


print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
