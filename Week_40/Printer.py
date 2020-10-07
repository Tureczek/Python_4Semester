import os
"""
3. Machine -> printer
Create a Machine class that takes care of powering on and off a the machine.
Create a printer class that is a subclass of the Machine super class.
The printer should be able to print to console.
The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.

"""
print("Turn machine on? Y/N")

class Machine:
    def __init__(self, onOff):
        self.onOff = onOff

    def __str__(self):
        return f"The printer i {self.onOff}!"

    @property
    def onOff(self):
        return self.__onOff

    @onOff.setter
    def onOff(self, x):
        if x == 'on':
            self.__onOff = 'ON'
        else:
            self.__onOff = 'OFF'

class Printer(Machine):
    def printOut(self, i, u):
        self.u = u

        if 'QUIT' not in i:
            return f"Printing out {i} on paper." + '\n' + f"Number of papers back in tray is {print(u)}"
        else:
            print('shutting down')
            os.exit()
        self.u += 1


    @property
    def u(self):
        self.u = 10
        return self.__u

    @u.setter
    def u(self):
        pass
class Papertray:
    def papers(self, paper):
        self.paper = paper
        return f"Numbers of papers left is {paper}"

    @property
    def paper(self):
        return self.__paper

    @paper.setter
    def paper(self, x):
        pass


