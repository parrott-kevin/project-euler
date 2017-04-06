# Problem 30

# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

p = 5
total = 0
for i in range(6 * 9**p, 2**p - 1, -1):
    n = str(i)
    num = 0
    for j in range(0, len(n)):
        num += int(n[j])**p
    if num == i:
        total += num
print(total)