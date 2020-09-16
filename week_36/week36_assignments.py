

# Sort a text
# Remove vowels and sort in alfabetical order
l = []

def sort_list(x):
    for i in x:
        if i in ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']:
            l.append(i)
            l.sort()
    return print(l)

sort_list('hello world')



#Ex 3: sort a list
    #Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
    #Sort this list by using the sorted() build in function.
    #Sort the list in reversed order.
    #Sort the list on the lenght of the name.
    #Sort the list based on the last letter in the name.
    #Sort the list with the names where the letter ‘a’ is in the name first.


a = ['Nicholas', 'Martin', 'Patrick', 'Victor']

#sortere alfabetisk
print(sorted(a))

#Sortere bagfra
print(sorted(a, reverse=True))

# sortere efter længden
print(sorted(a, key = len))

# sort list by last letter in the name:
#print(sorted(a, key = lambda x:x[-1]))
def sort_by_last(x):
    return x[-1]
print(sorted(a, key = sort_by_last))

#Sort the list with the names where the letter ‘a’ is in the name first.
#-----

print('Sort the list with the names where the letter ‘a’ is in the name first.')
def a_in(x):
    if 'a' in x.lower():
        return False
    return True
l = sorted(a, key=a_in)
sorted(l)





#for at åbne filen
#f = open('test.txt')
#print(f.read())
#print(f.r)

#Skriv til fil a for at tilføje
# s = open('test2.txt', 'w')
# s.write('Hello from my script file.')


#    1. Create a file and call it lyrics.txt (it does not need to have any content)
#    2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.
#    3. open and read the content and write it to your terminal window. * 
#       you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

# 1.
f = open("lyrics.txt", "w+")

# 2.
f1 = open("songs.docx", "w+")
f1.write("Mama, just killed a man" 
    "\nPut a gun against his head" 
    "\nPulled my trigger, now he's dead" 
    "\nMama, life had just begun" 
    "\nBut now I've gone and thrown it all away")
f1.close()

f1 = open("songs.docx", "r")
print("This is read()")
content = f1.read()
print(content, "\n")
f1.close()

f1 = open("songs.docx", "r")
print("This is readline()")
for line in f1:
    print(line)
f1.close()


f1 = open("songs.docx", "r")
print("\n")
content2 = f1.readlines()
print("This is readlines()")
print(content2)
f1.close()




# 1. Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
# 2. Sort the list so the result looks like this: [(1, 2), (1, 5), (2, 1), (2, 2), (2, 2), (3, 1), (3, 2), (10, 1), (10, 4)]

t = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
t.sort()
print(t)


x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']

z = x[1][2][1][2]
print(z)