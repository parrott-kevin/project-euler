# Problem 22

# What is the total of all the name scores in the file?


import csv


def nameval(word):
    """ Returns sum of a names letter values. """
    length = len(word) - 1
    i = 0
    value = 0
    while i <= length:
        value += ord(word[i]) - 96
        i += 1
    return value


# main
name_file = csv.reader(open('problem_22.txt', 'r'))
names = []
for i in name_file:
    names.extend(i)

names.sort()
i = 1
total = 0
for name in names:
    total += i * nameval(name.lower())
    i += 1
print(total)