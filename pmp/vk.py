class Student:
    def __init__(self, full_name, date_of_birth, address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address

    def display_full_name(self):
        return self.full_name


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, full_name):
        self.students = [student for student in self.students if student.full_name != full_name]

    def display_students(self):
        return [student.display_full_name() for student in self.students]


student1 = Student("Іванов Іван Іванович", "01.01.2000", "Київ, вул. Шевченка, 1")
student2 = Student("Петров Петро Петрович", "02.02.1999", "Львів, вул. Проспект Свободи, 2")

manager = StudentManager()

manager.add_student(student1)
manager.add_student(student2)

print("Список студентів:")
print(manager.display_students())

manager.remove_student("Іванов Іван Іванович")

print("Список студентів після видалення:")
print(manager.display_students())
