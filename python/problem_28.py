# Problem 28

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?


tot = 1
for base in range (3, 1003, 2):
    tot += 4 * base**2 - 6 * base + 6
print(tot)  