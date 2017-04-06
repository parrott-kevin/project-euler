# Problem 23

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.


import math
import time


def divisors(n):
    """ Returns the proper divisors of n. """
    ub = math.floor(math.sqrt(n))
    div = [1]
    for i in range(2, ub + 1):
        if n % i == 0:
            div.append(i)
            if n / i != i:
                div.append(n / i)
    return div


# main
st = time.time() 
abundant = []
sums = []
nums = []
for i in range(1, 20162):
    if sum(divisors(i)) > i:
        abundant.append(i)
for i in abundant:
    for j in abundant:
        sums.append(i + j)
for i in range(1, 20162):
    nums.append(i)
answer = list(set(nums).difference(set(sums)))
print(sum(answer), time.time() - st)
