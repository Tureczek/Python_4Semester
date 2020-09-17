import sys
import os

#Create a folder
directory = 'C:/Users/Nmtur/PycharmProjects/Python_4Semester/week_37/'

name = 'os_exercices'
path = directory+name

if not os.path.exists(name):
    os.mkdir(path)

os.chdir(path) #change directory

f = open('exercise.py', 'w')
g = open('exercise2.py', 'w')
# 3.

f.write(input('Write something to exercise 1:\n=> '))
g.write(input('Write something to exercise 2:\n=> '))
f.close()
g.close()

f = open('exercise.py', 'r')
g = open('exercise2.py', 'r')
print(f.read() + "\n" + g.read())

f,g.close()