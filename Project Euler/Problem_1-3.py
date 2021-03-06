from decorators import timer

'''
Euler problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def multiple(x, y, max):
    list = []
    original_x = x
    original_y = y

    while x <= max or y <= max:
        if x < max:
            list.append(x)
        x += original_x
        if y < max:
            list.append(y)
        y += original_y
    print(f'Euler problem 1: \nFind the sum of all the multiples of {original_x} or {original_y} below {max}. \n')
    print(list)
    return print(f'Sum of list: {sum(list)}')


# multiple(3, 5, 1000)
print("\n#################################################################################################################\n")

'''
Euler Problem 2:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''


def even_fibonacci_numbers():
    fib_sum = 0
    fibonacci_list = [0, 1]
    for i in range(2, 100):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    print(f'Fibonacci list : \n{fibonacci_list} \nSum of fibonacci list:\n{sum(fibonacci_list)}')

    for i in range(len(fibonacci_list)):
        if fibonacci_list[i] < 4_000_000 and (fibonacci_list[i] % 2 == 0):
            fib_sum += fibonacci_list[i]
            print(fibonacci_list[i])

    return print(f'fibonaci sum {fib_sum}')

even_fibonacci_numbers()

print("\n#################################################################################################################\n")

'''
Euler Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def prime_factors(n):
    i = 2
    original_n = n
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
        print(f'Largest primefactor of the number {original_n} is: {n}')
        return n

prime_factors(1000)

print("\n#################################################################################################################\n")
