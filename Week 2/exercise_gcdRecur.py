"""
Exercise: gcd recur
5/5 Points

Write a function, gcdRecur(a, b) that returns the greatest common divisor of two
positive integers recursively
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = None

    while gcd == None:
        if b == 0:
            gcd = a
            return gcd
        else:
            return gcdRecur(b, a%b)

    return gcd
