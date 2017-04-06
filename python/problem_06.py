# Problem 6

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

i = 1

sum_square = []
square_sum = []

while i <= 100:
    sum_square.append(i**2)
    square_sum.append(i)
    i += 1

print(sum(square_sum)**2-sum(sum_square))
