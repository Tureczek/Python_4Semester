# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    s_end = s[-3:]
    s_len = len(s)
    if s_end == 'ing':
        return f'{s}ly'
    if s_len < 3:
        return s[0:3]
    else:
        return  f'{s}ing'
  


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    substring_not = s.find('not')
    substring_bad = s.find('bad')

    if substring_not < substring_bad:
        s1 = s[0 : substring_not]
        s2 = s[-1 : substring_bad] 
        s3 = s[substring_bad+3:]
        s4 = f'{s1}{s2}good{s3}'
        return s4
    else:
        return s
  


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    a_length = len(a)
    b_length = len(b)
    
    a_front = a[0:a_length // 2] 
    a_back = a[a_length // 2:]
    if len(a_front) != len(a_back):
        a_front = a_front + a_back[0]
        a_back = a_back[1:]
        
    b_front = b[0:b_length // 2] 
    b_back = b[b_length // 2:]    
    if len(b_front) != len(b_back):
        b_front = b_front + b_back[0]
        b_back = b_back[1:]

    
    return a_front + b_front + a_back + b_back 


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (prefix + ' got: ' + got + ' expected: ' + expected)


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()