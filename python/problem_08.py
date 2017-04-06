# Problem 8

# Find the greatest product of five consecutive digits in the 1000-digit number.

num_file = open("problem_08.txt", "r")
num = str()
for line in num_file:
    num += line.strip('\n')
num_file.close()

i = 0
j = 5
total = 1
while j < 1000:
    m = 1
    for k in num[i:j]:
        m *= int(k)
    if m > total:
        total = m
    i += 1
    j += 1

print(total)
