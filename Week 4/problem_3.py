"""
Problem 3: Valid Words
10/10 Points

At this point we have not written any code to verify that a word given by a
player obeys the rules of the game. A valid word is in the word list; and it is
composed entirely of letters from the current hand. Implement the isValidWord
function.
"""
def isValidWord(word, hand, wordList):
    '''
    Returns True if word is in the wordList and is entirely composed of
    letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    '''
    copiedHand = hand.copy()
    valid = False

    if word in wordList:
        for char in word:
            copiedHand[char] = copiedHand.get(char, 0) - 1
            if copiedHand[char] < 0:
                valid = False
                break
            else:
                valid = True
    else:
        valid = False

    return valid
