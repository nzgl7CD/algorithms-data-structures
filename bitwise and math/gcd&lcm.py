def gcd(a:int,b:int)->int:
    '''
    Find the largest common factor of two ints
    '''
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a%b)

print(gcd(98,56))
