"""
Problem 4
15/15 Points

Write a Python function that takes in two lists and calculates whether they
are permutations of each other. The lists can contain both integers and
strings. We define a permutation as follows:
    the lists have the same number of elements
    list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.
If they are permutations of each other, the function returns a tuple consisting
of the following elements:
    the element occuring the most times
    how many times that element occurs
    the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one
element occurs the most number of times, you can return any of them.
"""
def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
        If they are permutations of each other, returns a
        tuple of 3 items in this order:
        the element occurring most, how many times it occurs, and its type
    """
    copyL1 = L1[:]
    maxNum = 0
    numCount = 0
    count = 0

    if len(L1) != len(L2):
        return False
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)

    for i in L2:
        if i in copyL1:
            count = copyL1.count(i)
            if count > numCount:
                numCount = count
                maxNum = i
            copyL1.remove(i)

    if len(copyL1) == 0:
        return (maxNum, numCount, type(maxNum))
    else:
        return False
