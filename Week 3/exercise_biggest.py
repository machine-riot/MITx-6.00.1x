"""
Exercsie: biggest
5/5 Points

We want to write some simple procedures that work on dictionaries to return
information.

This time, write a procedure, called biggest, which returns the key corresponding
to the entry with the largest number of values associated with it. If there is
more than one such entry, return any one of the matching keys.
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    largestCount = 0
    largestKey = None
    count = 0
    iter = 0

    if len(aDict) == 1:
        largestKey = list(aDict)[iter]
        return largestKey

    for i in aDict:
        count += len(aDict[i])
        if count >= largestCount:
            largestCount = count
            largestKey = list(aDict)[iter]
        iter += 1
        count = 0

    return largestKey
