from decorators import debug, timer, do_twice, repeat, count_calls, CountCalls

#Define class and decorating methods

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

#tw = TimeWaster(1000)
#print(tw.waste_time(999))


#Decorator recieving a class instead of a function
@timer
class TimeWaster2:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

"""Here, @timer only measures the time it takes to instantiate the class:"""
#tw2 = TimeWaster2(1000)
#print(tw2.waste_time(999))




#Decorating the whole class
from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str


# Nesting Decorators
"""Stacking decorators on top of each other:
Think about this as the decorators being executed
in the order they are listed. In other words, 
@debug calls @do_twice, which calls greet(), or debug(do_twice(greet())):
"""

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

#print(greet("Eva"))


@do_twice
@debug
def greet(name):
    print(f"Hello {name}")

#print(greet("Eva"))


# Decorators with Arguments
"""
@do_twice could be extended to a @repeat(num_times) decorator. 
The number of times to execute the decorated function could 
then be given as an argument.
"""
""" Used with repeat decorator on line 85 in decorators
@repeat(num_times = 4) 
def greet(name):
    print(f"Hello {name}")

#print(greet("World"))
"""

@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

#print(say_whee())
#print(greet("Penny"))

@count_calls
def say_whee():
    print("Whee!")

#print(say_whee())
#print(say_whee())


# Classes as Decorators
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")
"""
In terminal:

>>> counter = Counter()
>>> counter()
Current count is 1

>>> counter()
Current count is 2

>>> counter.count
2
"""

@CountCalls
def say_whee():
    print("Whee!")
#print(say_whee())
#print(say_whee())
#print(say_whee())
#print(say_whee())