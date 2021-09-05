"""
Exercise: is in
Points: 5/5

We can use bisection search to determine if a character is in a string, so
long as the string is sorted in alpabetical order.

First, test the middle character of a string against the character you're
looking for (the "test character"). If they are the same, we are done.

If they're not the same, check if the test character is "smaller" then the
middle character. If so, we need only consider the lower half of the string;
otherwise, we only consider the upper half of the string.

Implement the function isIn(char, aStr) which implements the above idea
recursively to test if char is in aStr. char will be a single character and aStr
will be a string that is in alphabetical order. The function should return a
boolean value.
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr)
    mid = len(aStr) // 2
    found = False

    if aStr == '':
        return found
    elif len(aStr) == 2:
        if aStr[0] == char or aStr[1] == char:
            found = True
            return found
        else:
            return found
    elif char == aStr[mid]:
        found = True
        return found
    elif char < aStr[mid]:
        return isIn(char, aStr[0:mid])
    else:
        return isIn(char, aStr[mid:len(aStr)])
