# Problem 2

# Find the sum of all the even-valued terms in the
# Fibonacci sequence which do not exceed four million.

i = 1
j = 0
fib = [1, 2]
fib_even = [2]

while fib[i] <= 4000000:
    j = fib[i] + fib[i-1]
    if j <= 4000000:
        fib.append(j)
        if j%2 == 0:
            fib_even.append(j)
    else:
        break
    
    i += 1
    

print(fib)
print(fib_even)
print(sum(fib_even))
    



