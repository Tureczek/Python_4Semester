""" Bank Exercise

Create a

* Bank class
* Account Class
* Customer class

The bank class should be able to hold many account.
You should be able to add new accounts.
The Account class should have relevant details.
The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.


"""

class Bank:
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, x):
        self.__accounts = x

    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, x):
        self.__no = x

    @property
    def cust(self):
        return self.__cust

    @cust.setter
    def cust(self, x):
        self.__cust = x

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        self.__name = x


"""
## Overloading
Add the abillity in your code to overload one or more init methods
"""

class Customer:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            self.name = args[0]
            self.age = args[1]
            self.gender = [2]


