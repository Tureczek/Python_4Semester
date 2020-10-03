"""
3. Machine -> printer
Create a Machine class that takes care of powering on and off a the machine.
Create a printer class that is a subclass of the Machine super class.
The printer should be able to print to console.
The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and and load new paper in the tray if empty.

"""

class Machine:
    def __init__(self, onOff):
        self.onOff = onOff
        print("Turn machine on? Y/N")
        inp = input()
        if inp == 'y':
            onOff == True
        else:
            onOff == False
        print(onOff)


class Printer(Machine):
    def __init__(self):
        pass
