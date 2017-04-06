# Problem 19

# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?


def months(m, y):
    """ Determines the length of the month. """
    if m == 4 or m == 6 or m == 9 or m == 11:
        length = 30
    elif m == 2:
        if y % 4 == 0:
            if str(y)[2:3] == "00" and y % 400 == 0:
                length = 29
            elif str(y)[2:3] != "00":
                length = 29
            else:
                length = 28
        else:
            length = 28
    else:
        length = 31
    return length


def days(d, n):
    """ Determines the days that make up the month. """
    freq = []
    for i in range(1, n + 1):
        if d > 7:
            d = abs(7 - d)
        freq.append(d)    
        d += 1
    last = freq[-1]
    if last == 7:
        start = 1
    else:
        start = last + 1
    return start
    

# main
year = 1901
day = 3
sun = 0
while year <= 2000:
    month = 1
    while month < 13:
        i = months(month, year)
        day = days(day, i)
        if day == 1:
            sun += 1
        month += 1
    year += 1
print(sun)
            