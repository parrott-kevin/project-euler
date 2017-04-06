# Problem 55

# How many Lychrel numbers are there below ten-thousand?


def reverse(n):
    """ Reverse a number. """
    m = int(str(n)[::-1])
    return m


def check(n):
    """ Compares n + reverse(n) to reverse(n + m). """ 
    m = reverse(n)
    p = n + m
    if p == reverse(p):
        return True
    return False


answer = 9999
for i in range(1, 10000):
    count = 1
    j = i
    while count < 50:
        if check(j):
            answer -= 1
            count = 50
        else:
            j += reverse(j)
            count += 1
print(answer)