from decorators import do_twice

#Simple function, returning value based on given argument
def add_one(number):
    return number + 1

#print(add_one(2))


#First-Class Objects
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, togetherwe are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

#print(greet_bob(say_hello))

#print(greet_bob(be_awesome))

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the secont_child() function")


    #second_child()
    #first_child()
#parent()

def parent1(num):
    def first_child():
        return "Hi, i am Emma"
    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
#Returning without the parantheses, returns a reference to the function and not the function itself
first = parent1(1)
second = parent1(2)
#print(first)
#print(second)

#It is possible to use the reference  as a regular expression

#print(first())
#print(second())




# Simple Decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

#say_whee = my_decorator(say_whee)
#say_whee()

""" New Decorator example dynamically changeable function
Does not run during night time.
"""

from datetime import datetime
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
#say_whee()
# This is the same as above.
# @my_decorator is the same as: say_whee = not_during_the_night(say_whee)

@my_decorator
def say_whee():
    print("Whee!")

#say_whee()


# importing method form other file.
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

#After changing decorators code ant adding *args, **kwarks it works with both
#say_whee()
#greet("World")


#Returning Values From Decorator Functions
#need the import too!

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

#hi_adam = return_greeting("Adam")
#The decorator is eating oure return value here adding: return func(*args, **kwarks) in decorators fixes it
#print(hi_adam)

#return_greeting("Adam")