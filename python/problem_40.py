# Problem 40

# If dn represent the nth digit of the fractional part, find the value of the
# following expression.
#           d1 * d10 * d100 * 1000 * d10000 * d100000 * d10000000

i = 0
j = ""
k = 1
answer = 1
while len(j) <= 1000000:
    j += str(i)
    if len(j)-1 >= k:
        answer *= int(j[k])
        k *= 10
    i += 1
print(answer)    