# Problem 1

# Find the sum of all the multiples of 3 or 5 below 1000.

test = []

for i in range(1, int(999/3)+1, 1):
    if i*3%5 != 0:
        test.append(i*3)

for i in range(1, int(999/5)+1, 1):
    test.append(i*5)

test.sort()
print(test)
print(sum(test))
