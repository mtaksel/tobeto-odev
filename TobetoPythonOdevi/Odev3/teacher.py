class Teacher:
    def __init__(self,name,surname,department,age) -> None:
        self.name = name
        self.surname = surname 
        self.department = department
        self.age = age

    def teacher_info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Department: {self.department}, Age: {self.age}"
        
    def teach(self):
        return f"{self.name} is teaching..."

