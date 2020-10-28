class Car:
    def __init__(self, *args):
        self.make = args[0]
        self.model = args[1]
        self.bhp = args[2]
        self.mph = args[3]

    @property #Getter
    def make(self):
        return self.__make

    @make.setter
    def make(self, x):
        self.__make = x

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, x):
        self.__model = x

    @property
    def bhp(self):
        return self.__bhp

    @bhp.setter
    def bhp(self, x):
        self.__bhp = x

    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, x):
        self.__mph = x
