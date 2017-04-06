# Problem 39

# For which value of p <= 1000, is the number of solutions maximised?


import math


def perimeter(p):
    """ Determines all a, b, c values of triangle with perimeter, p. """
    ans = []
    for a in range(1, p // 2 + 1):
        for b in range(a, (p - a) // 2 + 1):
            c = (a**2 + b**2)**.5
            if a + b + c == p:
                ans.append([a, b, c])
    return len(ans)


# main
len_answer = 0
for i in range(4, 1000):
    if perimeter(i) > len_answer:
        len_answer = perimeter(i)
        answer = (i, perimeter(i))
print(answer)