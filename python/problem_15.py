# Problem 15

# How many routes are there through a 20x20 grid?

n = 1
k = 1
for i in range(1, 41):
    n *= i
for i in range(1, 21):
    k *= i

ncr = n / (k * k)
print(int(ncr))