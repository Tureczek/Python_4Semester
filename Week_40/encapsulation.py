class P:
    def __init__(self, name, alias):
        self.name = name #slef.name er nu en property
        # self.__alias = alias #Privat instance variable p._P__alias <- m�den at f� fat i den p�
        self.alias = alias

    @property  # Getter
    def name(self):
        return self.__name

    @name.setter  # Setter
    def name(self, x):
        if x[0] == 'C': #Denne type af tjek, er en del af encapsulation
            self.__name = x
        else:
            self.__name = 'CCCC!!!'
"""
        @property
        def alias(self):
            return self.__alias

        @alias.setter
        def alias(self, x):
            self.__alias = x
"""


#Bad java style

"""
    def get_alias(self):
        return self.__alias

    def set_alias(self, x):
        self.__alias = x

    def get_name(self, name):
        return self.name

    def set_name(self, x):
        self.name = x

"""
