class Student:
    def __init__(self,name,surname,studentNumber,age):
        self.name = name
        self.surname = surname 
        self.studentNumber = studentNumber
        self.age = age

    def student_info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Student Number: {self.studentNumber}, Age: {self.age}"

    def doHomework(self):
        return f"{self.name} is doing homework"
