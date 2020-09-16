import sys
import os

#Create a folder
directory = 'C:/Users/Nmtur/PycharmProjects/Python_4Semester/week_37/'

name = 'os_exercices'
path = directory+name

if not os.path.exists(name):
    os.mkdir(path)

#os.chdir(path)

f = open('exercise.py', 'w')

# 3.

f.write(input('Write something:\n=> '))