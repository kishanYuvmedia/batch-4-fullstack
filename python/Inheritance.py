class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super_introduction = super().introduce()
        print(super_introduction)  # Call the parent class's introduce
        return f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}."
    

student=Student("Alice", 20, "S12345")
print(student.introduce())
