# Problem 12

# What is the value of the first triangle number to have over five hundred
# divisors?


import math


def tri_num(n):
    tri = 0
    for i in range(1, n + 1, 1):
        tri += i
    return tri

def divisors(n):
    sqrt_n = math.floor(math.sqrt(n))
    if n != 1:
        div = [1, n]
        for i in range(1, sqrt_n, 1):
            if n % i == 0:
                div.append(n)
                div.append(n/i)
    else:
        div = [1]
    return div

# main
tri_list = []
i = 1
j = 0
length = 0
while length <= 500:
    tri_list.append(tri_num(i))
    length = len(divisors(tri_list[j]))
    i += 1
    j += 1
print(tri_list[j - 1], length)