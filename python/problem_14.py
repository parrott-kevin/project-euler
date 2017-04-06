# Problem 14

# Which starting number, under one million, produces the longest chain?


import math


def collatz(n):
    """ Determine next number in the sequence. """
    if n % 2 == 0:
        num = n / 2
    else:
        num = 3 * n + 1 
    return num


# main
i = 13
maximum = 0
max_num = 0

while i < 1000000:
    j = i
    k = math.log(j,2)
    count = 1
    if k != int(k):
        while j != 1:
            j = collatz(j)
            count += 1
        if count > maximum:
            maximum = count
            max_num = i
    i += 2

print(max_num, maximum)