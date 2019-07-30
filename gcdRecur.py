def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a==1 or b==1:
        return 1
    if a==b:
        return a # or can return b
    if a<b:
        # a<b
        if b%a == 0:
            return a
        else:
            return gcdRecur(a,b%a)
    else:
        # b<a
        if a%b == 0:
            return b
        else:
            return gcdRecur(a%b,b)



print(gcdRecur(9,12))
