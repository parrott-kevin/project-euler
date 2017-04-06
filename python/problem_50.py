# Problem 50

# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

import time

def primality(n):
    """ Checks for primality. """
    m = int(n**.5)
    for i in range(2, m + 1):
        if n % i == 0 and n != i:
            return False
    return True

st = time.clock()

primes = [2]
i = 3
fin = 1000000
greatest = 0
while i < fin:
    if primality(i):
        primes.append(i)
        if primality(sum(primes)):
            if sum(primes) > greatest and sum(primes) < fin:
                greatest = sum(primes)
                length = len(primes)
    i += 2
print(primes[length-1])
#
#i = 0
#j = length
#done = False
#while not done:
#    total = sum(primes[i:j])
#    if total > greatest and total < fin and (j - i) >= length:
#        if primality(total):
#            greatest = total
#            length = j - i
#    if sum(primes[i:j + 1]) < fin:
#        j += 1
#    else:
#        i += 1
#        j = i + length
#    if j >= len(primes) or i >= j or total >= fin:
#        done = True
#        
#print(greatest, length, time.clock() - st)
