from decorator_exercise import time_stamp, print_twice, take_time, slow_down

@take_time
@time_stamp
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
"""
print(add(1))
print(add(9))
print(add(4))
print(add(5))
"""

@take_time
@time_stamp
#@print_twice
def printer(text):
    return text + ' ' + text

#print(printer("HEllo"))

@slow_down
def countdown(n):
    if not n: # 0 is false, not false is true
        return n
    else:
        print(n, end=' ')
        return  countdown(n-1) # call the same function with n as one less

print(countdown(3))