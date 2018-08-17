#!/usr/bin/env python3


class SchoolMember:
    'Represent any school member'
    def __init__(self, name, age):
        self.name  = name
        self.age = age
        print("Initialized SchoolMember: {}".format(self.name))

    def tell(self):
        'Tell my details.'
        print('Name: {} Age: {}'.format(self.name, self.age))


class Teacher(SchoolMember):
    'Represents a teacher'
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: U$S{:d}'.format(self.salary))


class Student(SchoolMember):
    'Represents a Student.'
    def __init__(self, name, age,marks):
        SchoolMember.__init__(self,name, age)
        self.marks  = marks
        print('Initialized Student: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))


t = Teacher('Sr Fabio', 40, 12000)
s = Student('Srta Juliana', 40, 75)
print()

members = [t,s]
for member in members:
    member.tell()
