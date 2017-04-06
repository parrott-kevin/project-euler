# Problem 20

# Find the sum of the digits in the number 100!


import math

def digit_sum(n):
    digit = 0
    for i in str(n):
        digit += int(i)
    return digit

# main
num = math.factorial(100)
print(digit_sum(num))
