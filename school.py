class Student:
    def __init__(self, name, class_no, id):
        self.name = name
        self.class_no = class_no
        self.id = id

    def __repr__(self):
        return f'Student with name {self.name}, class {self.class_no}, id {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher with name {self.name}, subject {self.subject}, id {self.id}'    


mukto = Student("Mukto", 10, 2312)
mukto_2 = Teacher("Puppu", "Math", 8856)
print(mukto)
print(mukto_2)
