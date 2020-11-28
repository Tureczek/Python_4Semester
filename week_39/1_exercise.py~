from inst import Instructor

class Person:

    type = 'Mammel'

    #def __init__(self, name, last, age=None):
     #   self.name = name
      #  self.last = last
       # self.age = age
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        if len(args) == 2:
            self.name = args[0]
            self.last = args[1]
        else:
            raise Exception()


    #Laver en ny metode, sker gennem en ny funktion
    def full_name(self):
        return self.name + ' ' + self.last #+ ' ' + self.funny

    def funny_Age(self):
        self.funny = 'Ha ha ha'


class Gender:
    def __init__(self, s):
        self.sex = s

#Arver fra Instructor
class Student(Instructor):
    def __init__(self, *args):
        #super().__init__(args[0])
        Instructor.__init__(self, args[0])
        Gender.__init__(self, args[1])
        self.salary = args[2]




#Test#

#p = Person('Nicholas', 'TureczeK')

#print(p.full_name())
#print(p.__dict__)
