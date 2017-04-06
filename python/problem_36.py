# Problem 36

# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.


import math


def palindrome(n):
    """ Checks if number is a palindrome. """
    n = str(n)
    rn = n[::-1]
    if n == rn:
        return True
    

def binary(n):
    """ Converts number to binary. """
    num = ""
    while n >= 1:
        r = n % 2
        num = str(r) + num
        n = math.floor(n / 2)
    return num


# main
j = 0
for i in range(1, 1000000, 2):
    if palindrome(i) and palindrome(binary(i)):
        j += i
print(j)

