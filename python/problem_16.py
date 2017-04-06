# Problem 16

# What is the sum of the digits of the number 2**1000?


def digit_sum(n):
    digit = 0
    for i in str(n):
        digit += int(i)
    return digit

# main
num = 2**1000
print(digit_sum(num))
