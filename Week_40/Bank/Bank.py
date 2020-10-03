"""

2. Bank
In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.
The bank class should futher be change into not taking any accounts as parameters at initialization. The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).
Somewhere you should change the code so that a customer only can create one account.
The Customer class should make sure that the customer is over 18 year of age.

"""

class Bank:
    def __init__(self):
        self.__accounts = []  # initialize the private variable as a list

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, acc):
        self.__accounts.append(acc)


class Account:
    def __init__(self, no, cust):
        self.__no = no
        self.__cust = cust
    def __repr__(self):
        return str(self.__dict__)


class Customer:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return str(self.__dict__)


