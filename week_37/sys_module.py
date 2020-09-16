import sys

def check_syntax(x):    
    if '-it' in x and '-rm' in x:
        print('Cool story bro!')
    elif "-it" not in x:
        print('not okay!')
    elif '-it' in x:
        print("Thats cool!")


check_syntax(sys.argv)
    