"""
Problem 3: Printing Out all Available Letters
10/10 Points

Next, implement the function getAvailableLetters that takes in one parameter -
a list of letters, lettersGuessed. This function returns a string that is
comprised of lowercase English letters - all lowercase English letters that are
not in lettersGuessed.

Example usage:
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have
        not yet been guessed.
    '''
    return ''.join(x for x in 'abcdefghijklmnopqrstuvwxyz' if x not in lettersGuessed)
