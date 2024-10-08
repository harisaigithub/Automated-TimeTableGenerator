class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Admin(User):
    def __init__(self, name):
        super().__init__(name, role="admin")

class Teacher(User):
    def __init__(self, name, subjects, available_times):
        super().__init__(name, role="teacher")
        self.subjects = subjects
        self.available_times = available_times

class Student(User):
    def __init__(self, name, class_section):
        super().__init__(name, role="student")
        self.class_section = class_section
