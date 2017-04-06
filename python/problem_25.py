# Problem 25

# What is the first term in the Fibonacci sequence to contain 1000 digits?


def fibonacci(n1, n2):
    next = n1 + n2
    return next


# main
fib = [1, 1]
i = 1
length = 0
while length != 1000:
    fib.append(fibonacci(fib[i-1], fib[i]))
    length = len(str(fib[-1]))
    i += 1
    
print(len(fib))
