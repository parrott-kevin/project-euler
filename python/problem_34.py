# Problem 34

# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.

import math

numbers = []
for i in range(3, math.factorial(9)):
    num = str(i)
    total = 0
    for j in range(0, len(num)):
        total += math.factorial(int(num[j]))
    if total == i:
        numbers.append(i)
print(sum(numbers))