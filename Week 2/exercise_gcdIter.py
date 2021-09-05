"""
Exercise: gcd iter
5/5 Points

Write an iterative function, gcdIter(a, b), that returns the greatest common
divisor of two positive integers.
"""
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smallest = 0
    gcd = 0

    if a < b:
        smallest = a
    else:
        smallest = b

    while smallest != 0:
        if a%smallest == 0 and b%smallest == 0:
            return smallest
        else:
            smallest -= 1
