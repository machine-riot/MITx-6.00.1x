"""
Problem 1: Is the Word Guessed
10/10 Points

We'll start by writing 3 simple functions that will help us easily code the
Hangman problem. First, implement the function isWordGuessed that takes in
two parameters - a string, secretWord, and a list of letters, lettersGuessed.
This function returns a boolean - True if secretWord has been guessed (ie, all
the letters of secretWord are in lettersGuessed) and False otherwise.

example usage:
>>> secretWord = 'apple'
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False

For this function, you may assume that all the letters in secretWord and
lettersGuessed are lowercase.
"""
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in
        lettersGuessed; False otherwise
    '''
    guessed = False

    for char in secretWord:
        if char in lettersGuessed:
            guessed = True
        if char not in lettersGuessed:
            guessed = False
            break

    return guessed
