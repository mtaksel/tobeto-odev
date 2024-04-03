from student import Student
from teacher import Teacher

students = []
teachers = []

def add_student(name,surname,studentNumber,age):

    student = Student(name,surname,studentNumber,age)
    students.append(student)

def add_teacher(name,surname,department,age):

    teacher = Teacher(name,surname,department,age)
    teachers.append(teacher)

def list_students():
    print("Students:")
    for Student in students:
        print(Student.student_info())

def list_teachers():
    print("Teachers:")
    for Teacher in teachers:
        print(Teacher.teacher_info())


add_student("Zehra", "Şentürk", 1020, 23)
add_student("Muhsine", "Taşçi", 2020, 23)
add_student("Tuba", "Bezek", 2030, 23)
add_teacher("Mehmet Turgut", "Aksel", "Test", 23)
add_teacher("Muhsine", "Taşçi", ".NET", 23)

list_students()
list_teachers()
