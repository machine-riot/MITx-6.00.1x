"""
Exercise: polysum
10/10 Points

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25*n*s^2)/tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s. This
function should sum the area and square of the perimeter of the regular
polygon. The function returns a sum, rounded to 4 decimal places.
"""
def polysum(n, s):
    '''
    n: a positive integer
    s: a positive integer or float

    returns: a positive integer or float, sum of the area and square of the
    perimeter of a regular polygon.
    '''
    import math

    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n*s

    return round(area + (perimeter**2), 4)
