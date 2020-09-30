#Create a Bank, an Account, and a Customer class.
#All classes should be in a single file.
#The bank class should be able to hold many account.
#You should be able to add new accounts.
#The Account class should have relevant details.
#The Customer class Should also have relevant details.
#Stick to the techniques we have covered so far.



class Bank:

    def __init__(self):
        self.accounts = []
        


class Account:

    def __init__(self, no, cust):
        self.no = no
        self.cust = cust


class Costumer:

    def __init__(self, name):
        self.name = name
