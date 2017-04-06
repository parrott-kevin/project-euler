# Problem 38

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1, 2, ..., n) where n >= 1?


def prods(m):
    """ Return n (m * p) and check for pandigitaly. """
    done = False
    n = ""
    p = 1
    while not done:
        n += str(m * p)
        if len(n) >= 9:
            done = True
        p += 1
    i = []
    for j in n:
        i.append(j)
    i.sort()
    k = ""
    for j in i:
        k += j
    if k != "123456789":
        return 0
    return int(n)


# main
num = 0
answer = 0        
for i in range(1, 10000):
    if prods(i) > answer:
        answer = prods(i)
        num = i
print(num, answer)