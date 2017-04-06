# Problem 4

# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome(n):
    """ Checks if number is a palindrome. """
    n = str(n)
    i = 0
    j = len(n)-1
    while i != len(n)-1:
        if n[i] == n[j]:
            i += 1
            j -= 1
            k = True
        else:
            k = False
            break
    return k


# main
done = 0
for p1 in range(999, 99, -1):
    for p2 in range(999, 99, -1):
        product = p1 * p2
        if palindrome(product):
            if done < product:
                done = product
                dp1 = p1
                dp2 = p2
                
print(dp1, dp2, done)            
            

        
    
            
            
    
            
