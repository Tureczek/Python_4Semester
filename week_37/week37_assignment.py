#------------------ List Comprehension ------------------------#

#Samme måde at lave listen på.
list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
list2 = [chr(i) for i in range (65, 91)]
#70, 75, 80, 85

# går listen igennem, og ekskludere [70, 75, 80, 85]
l3 = [chr(i) for i in range (65, 91) if not i in [70, 75, 80, 85]]
print(list2)
print(l3)

#---#
print([i for i in range(1,10) if i%2 ==0])



#----------------- Moduls -----------------#

import sys

def message(x):
    if len(x) > 0:
        print(x[1])
    
    if len(x) > 1:
        print(x[2])
        print(x[3])
message(sys.argv)
