"""
Problem 1 - Word Scores
10/10 Points

The function getWordScore should accept as input a string of lowercase letters
(a word) and return the integer score for that word, using the game's scoring
rules.
"""
def getWordScore(word, n):
    '''
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sym of the points for letters in the word,
    multiplied by the length of the word, PLUS 50 points if all n letters are
    used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3,
    and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    '''
    wordScore = 0

    for char in word:
        wordScore += SCRABBLE_LETTER_VALUES[char]
    wordScore *= len(word)

    if len(word) == n:
        wordScore += 50

    return wordScore
