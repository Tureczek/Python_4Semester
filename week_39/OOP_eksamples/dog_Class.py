# A class is a blueprint for how something should be defined. It doesn’t actually contain any data.
# .__init__() is a method initializing each new instance of the class

class Dog:
    #Class attribute : Class attributes are defined directly beneath the first line of the class name.
    species = "Canis familiaris"


    def __init__(self, name, age):
        self.name = name
        self.age = age
    """
    self.name = name creates an attribute called name and assigns to it the value of the name parameter.
    self.age = age creates an attribute called age and assigns to it the value of the age parameter.
    - Attributes created in .__init__() are called instance attributes
    """

