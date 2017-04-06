# Problem 7

# What is the 10001st prime number?


import math


def check_prime(n):
    j = math.floor(math.sqrt(n))

    prime = True
    for k in range(3, j+1, 1):
        if n % k == 0:
            prime = False
            break
    return prime


# main
i = 2
j = 3

while i <= 10001:
    if check_prime(j):
        if i == 10001:
            print(j)
        i += 1
    j += 2
    


