# Problem 17

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?


numbers = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five",
           6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten",
           11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen",
           15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen",
           19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty",
           50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty",
           90 : "ninety", 1000 : "onethousand"}


def minor(n):
    """ Returns the word of the given number for numbers under 21. """
    return numbers[n]
    

def underhundred(n):
    """ Returns the word of a number under one hundred. """
    if 20 < n < 100 and n % 10 != 0:
        p0 = int(str(n)[0] + "0")
        p1 = int(str(n)[1])
        return numbers[p0] + numbers[p1]
    if 20 < n < 100 and n % 10 == 0:
        return numbers[n]    


def overhundred(n):
    """ Returns the word of a number over and including one hundred. """
    if n != 1000:
        p0 = int(str(n)[0])
        rnd = int(str(p0) + "0" + "0")
        fin = n - rnd
        first = str(minor(p0)) + "hundredand"
        if n != rnd and fin < 10:
            p2 = int(str(n)[2])
            return first + str(minor(p2))
        elif fin >= 10 and n != rnd:
            p12 = int(str(n)[1:])
            if fin > 20:
                return first + str(underhundred(p12))
            else:
                return first + str(minor(p12))               
        else:
            return str(minor(p0)) + "hundred"
    else:
        return numbers[n]
    

# main    
i = 1
total = ""
while i <= 1000:
    if i <= 20:
        total += minor(i)    
    if 20 < i < 100: 
        total += underhundred(i)
    if i >= 100:
        total += overhundred(i)
    i += 1
print(len(total))