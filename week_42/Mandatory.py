import datetime
# Model an organisation of employees, management and board of directors in 3 sets.

directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}


# 1.1 who in the board of directors is not an employee?
def assignment1_1():
    print("Assignment 1.1 who in the board of directors is not an employee?")
    result = [i for i in directors if i not in employees]
    print(f"This is the directors which is not in the employees set: {result} \n")

    # for x in directors:
    #    if x not in employees:
    #        print(x)


# 1.2 who in the board of directors is also an employee?
def assignment1_2():
    print("1.2 who in the board of directors is also an employee?")
    result = [i for i in directors if i in employees]
    print(f"This is the directors which is also in the employees set: {result} \n")


# 1.3 How many of the management is also member of the board?
def assignment1_3():
    print("1.3 How many of the management is also member of the board?")
    result = len([i for i in management if i in directors])
    print(f"This is the manager which is also in the board set: {result}\n")


# 1.4 All members of the managent also an employee
def assignment1_4():
    print("1.4 All members of the managent also an employee")
    result = [i for i in management if i in employees]
    print(f"This is the manager which is also in the employee set: {result}\n")


# 1.5 All members of the management also in the board?
def assignment1_5():
    print("1.5 All members of the management also in the board?")
    result = [i for i in management if i in directors]
    print(f"This is the manager which is also in the board set: {result}\n")


# 1.5 Who is an employee, member of the management, and a member of the board?
def assignment1_6():
    print("1.5 Who is an employee, member of the management, and a member of the board?")
    result = [i for i in employees if i in management and directors]
    print(f"This is the manager which is also in the board and employee set: {result}\n")


# 1.7 Who of the employee is neither a memeber or the board or management?
def assignment1_7():
    print("1.7 Who of the employee is neither a memeber or the board or management?")
    result = [i for i in employees if i not in management and directors]
    print(f"This is the manager which is not in the board and neither in the employee set: {result}\n")


# 2.0 Using a list comprehension create a list of tuples from the folowing datastructure
def assignment2_0():
    print("2.0 Using a list comprehension create a list of tuples from the folowing datastructure")
    dictList = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
    tupelList = [(k, v) for k, v in dictList.items()]
    print(tupelList)
    print("")


# From these 2 sets:
# {'a', 'e', 'i', 'o', 'u', 'y'}
# {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
# Of the 2 sets create a: Union, Symmetric Difference, Difference and disjoint

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

def union():
    print("Union")
    unionSet = set1.union(set2)
    print(f"Union set of set1: {set1}, \n and set2: {set2}, \n is: {unionSet}\n")

def symmetric_difference():
    print("symmetric difference")
    sd_set = set1.symmetric_difference(set2)
    print(f"symmetric difference set of set1: {set1}, \n and set2: {set2}, \n is: {sd_set}\n")

def difference():
    print("difference")
    differenceSet = set1.difference(set2)
    differenceSet2 = set2.difference(set1)
    print(f"Difference of {set1}, \n and {set2}, \n is: {differenceSet}\n")
    print(f"The difference set of set2: {set2}, \n and set1: {set1}, \n is: {differenceSet2}\n")

def disjoint():
    print("disjoint")
    print("first check if disjoint. If true they have nothing in common, if false they have something in common")
    isdisjoint = set1.isdisjoint(set2)
    print(f"Is it disjoint? {isdisjoint}")
    disjointSet = set1.intersection(set2)
    print(f"Disjoint set of {set1}, \n and {set2}, \n is: {disjointSet}\n")

# 4 Date Decoder
monthDict = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12"
}

testDate = "8-MAR-85"

def stringSplitter(testDate):
    print("Date Decoder")

    substring = testDate.split("-")
    substring[1] = monthDict[substring[1]]


    if int(substring[2]) > 20:
        substring[2] = "19" + substring[2]
    else:
        substring[2] = "20" + substring[2]
    print(tuple(substring[::-1]))
    return substring[::-1]




assignment1_1()
assignment1_2()
assignment1_3()
assignment1_4()
assignment1_5()
assignment1_6()
assignment1_7()
assignment2_0()
union()
symmetric_difference()
difference()
disjoint()
stringSplitter(testDate)