#----------Alphabetic List comprehension --------#


# går listen igennem, og ekskludere [70, 75, 80, 85]
#l3 = [chr(i) for i in range (65, 91) if not i in [70, 75, 80, 85]]
#print(l3)
l4 = [chr(i) for i in range (65, 91) if not i in range (70, 80, 2)]
print(l4)

#---#




#----------------Clothes List --------------#
colors = ['black', 'white', 'Green', 'Red']
size = ['s', 'm', 'l','xl']


new_list = [(i, j) for i in colors for j in size]

print(new_list)

#------------ Ex 2. Sort a text ------------#

	
def sort_cons2(s):
    s = [i for i in s.lower() if not i in ('a', 'e', 'i', 'o', 'u', 'y', ' ')]
    return sorted(s)
print(sort_cons2('Hello World'))