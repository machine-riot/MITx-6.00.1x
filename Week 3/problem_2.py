"""
Problem 2: Getting the User's Guess
10/10 Points

Next, implement the function getGuessedWord that takes in two parameters - a
string, secretWord, and a list of letters, lettersGuessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in lettersGuessed are in secretWord. This shouldn't be too different
from isWordGuessed!

Example usage:
>>> secretWord = 'apple'
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
"""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
    '''
#    guessedWord = ''

#    for char in secretWord:
#        if char in lettersGuessed:
#            guessedWord += char
#        else:
#            guessedWord += '_ '

#    return guessedWord
    return ''.join(n if n in lettersGuessed else '_ ' for n in secretWord)

# Commented out my initial solution which worked, but then included my solution
# for the additional challenge of solving this with one line of code.
