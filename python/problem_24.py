# Problem 24

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?


import math


num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number = []
total = 0
n = 1000000
i = 9
j = 1
while i > 0:
    if total + j * math.factorial(i) >= n:
        k = num[j - 1]
        number.append(k)
        total += (j - 1) * math.factorial(i)
        num.remove(k)
        i -= 1
        j = 1
    j += 1
number.append(num[0])
print(number)