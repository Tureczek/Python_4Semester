# Reading Large Files
# Count the number of rows in a CSV file.
"""
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
"""


# This is for large csv files <- turned it in to a generator function

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


"""
    Using yield will result in a generator object.
    Using return will result in the first line of the file only.
"""

# define a generator expression (also called a generator comprehension), which has a very similar syntax to list comprehensions.

csv_gen = (row for row in open("techcrunch.csv"))  # Generator comprehension
# csv_gen = csv_reader("techcrunch.csv") # Lazy iterator

row_count = 0

for row in csv_gen:
    row_count += 1

print(f"row count is {row_count}")


# Generating an Infinite Sequence

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#     print(i, end=" ")

"""
The program will continue to execute until you stop it manually.
Instead of using a for loop, you can also call next() on the generator object directly. This is especially useful for testing a generator in the console:

>>> gen = infinite_sequence()
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
"""


# Detecting Palindromes
# Palindromes: words or numbers that are read the same forward and backward, like 121

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


"""
for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        print(pal)
"""

"""
Generator functions look and act just like regular functions, 
but with one defining characteristic. 
Generator functions use the Python yield keyword instead of return.

yield indicates where a value is sent back to the caller, 
but unlike return, you don’t exit the function afterward.
Instead, the state of the function is remembered.

You’ll have no memory penalty when you use generator expressions.
"""

##########################################################################################################

# Profiling generator preformance

import sys

nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

"""
In this case, the list you get from the list comprehension
is 43,808 bytes, while the generator object is only 56. 
This means that the list is over 500 times larger than the generator object!

There is one thing to keep in mind, though. If the list is smaller 
than the running machine’s available memory, then list comprehensions 
can be faster to evaluate than the equivalent generator expression.
"""

##########################################################################################################


import cProfile

print(cProfile.run('sum([i * 2 for i in range(10000)])'))  # lc
print(cProfile.run('sum((i * 2 for i in range(10000)))'))  # gc

"""
Here, you can see that summing across all values in the list comprehension 
took about a third of the time as summing across the generator. If speed is 
an issue and memory isn’t, then a list comprehension is likely a better tool for the job.
"""

##########################################################################################################

# StopIteration

letters = ["a", "b", "c", "d"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)


##########################################################################################################

# Using Advanced Generator Methods

"""
Methods for generator objects:

    .send()
    .throw()
    .close()
"""


# How to Use .send()

def is_palindrome2(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome2(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

"""
pal_gen_send = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits)) # print
"""

# How to Use .throw()
"""
pal_gen_throw = infinite_palindromes()
for i in pal_gen_throw:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen_throw.throw(ValueError("We don't like large palindromes")) # Here we use .throw()
    pal_gen_throw.send(10 ** (digits)) # Here we use .send()
"""
"""
.throw() is useful in any areas where you might need to catch an exception. 
In this example, you used .throw() to control when you stopped iterating 
through the generator. You can do this more elegantly with .close().
"""

# How to Use .close()
"""
pal_gen_close = infinite_palindromes()
for i in pal_gen_close:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen_close.close()
    pal_gen_close.send(10 ** (digits))
"""


##########################################################################################################

"""
What is gonna happen:

    1 Read every line of the file.
    2 Split each line into a list of values.
    3 Extract the column names.
    4 Use the column names and lists to create a dictionary.
    5 Filter out the rounds you aren’t interested in.
    6 Calculate the total and average values for the rounds you are interested in.

"""

#reading each line from file:

file_name = "techcrunch.csv"
lines = (line for line in open(file_name))

# Generator expression to split each line into a list
list_line = (s.rstrip().split(",") for s in lines)

# Since the column names tend to make up the first line in a CSV file, you can grab that with a short next() call
cols = next(list_line)

"""
To sum this up, you first create a generator expression lines to yield each line in a file. 
Next, you iterate through that generator within the definition of another generator expression 
called list_line, which turns each line into a list of values. 
Then, you advance the iteration of list_line just once with next() to get a list of the column names from your CSV file
"""

company_dicts = (dict(zip(cols, data)) for data in list_line)

"""
This generator expression iterates through the lists produced by list_line. 
Then, it uses zip() and dict() to create the dictionary as specified above
"""

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

"""
In this code snippet, your generator expression iterates through the results of company_dicts and 
takes the raisedAmt for any company_dict where the round key is "a".

Callinmg sum() to iterate through funding 
"""
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")

"""
BREAKDOWN:


    Line 246 reads in each line of the file.
    Line 249 splits each line into values and puts the values into a list.
    Line 252 uses next() to store the column names in a list.
    Line 261 creates dictionaries and unites them with a zip() call:
        The keys are the column names cols from line 252.
        The values are the rows in list form, created in line 249.
    Line 268 gets each company’s series A funding amounts. It also filters out any other raised amount.
    Line 280 begins the iteration process by calling sum() to get the total amount of series A funding found in the CSV.

"""