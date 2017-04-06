# Problem 56

# Considering natural numbers of the form a**b where a & b < 100, what is the
# maximum digital sum

def digit_sum(n):
    """ Sum the digits of n. """
    m = str(n)
    d = 0
    for i in range(0, len(m)):
        d += int(m[i])
    return d


# main
answer = 0
for i in range(1, 100):
    for j in range(1, 100):
        k = i**j
        if digit_sum(k) > answer:
            answer = digit_sum(k)
print(answer)