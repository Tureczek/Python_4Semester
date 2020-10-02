class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    #def description(self):
    #    return f"{self.name} is {self.age} years old"
    """
    Replacing description() method with a __str__()
    so when we type print(miles) we get more information.
    !! Methods like __init__() and __str__() are called dunder methods !!
    """
    def __str__(self):
        return f"{self.name} is {self.age} years"


    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


