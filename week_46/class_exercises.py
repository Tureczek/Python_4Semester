
# ex1 Python Students
"""
Based on the Student class below, create a PythonStudents class that acts as a collection of students.
The class should implement the iterations functionality (iter() and next()) and be able to return
an iter object. When iterated the Pythod_students object should return the name of each student in the list.
"""

class pythonStudents:
    ()
    pass

class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name.capitalized()

    def __add__(self, student):
        return Student('Anna the daughter', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
        return f'self.__dict__'


