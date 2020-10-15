def msg(x):
    print('Hello ', x)


msg('Nicholas')

print(list('abcde' + 'fghi')[3:6])

s = "Nicholas"
print(s[::-5])

spam = 10


def test():
    spam = 20
test()

print(spam)
print("15" * 10)

def first(n):
    num = 1
    sum = 0
    
    while num < n + 1:
        sum = sum + num
        num = num + 1
        print(sum)
    return sum

