# Problem 9

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def triplet(d):
    for a in range(1, d, 1):
        for b in range(a+1, d, 1):
            if a**2 + b**2 == (d - a - b)**2:
                return a, b

# main
num = 1000
i, j = triplet(num)

k = (i**2 + j**2)**.5
total = i * j * k
print(i, j, k, total)
