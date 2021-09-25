"""
Problem 2: Dealing with Hands
10/10 Points

The player starts with a hand, a set of letters. As the player spells out words,
letters from this set are used up. For example, the player could start out
with the following hand: a, q, l, m, u, i, l. The player could choose to spell
the world quail. This would leave the player's hand: l, m. Your task it to
implement the function updateHand, which takes in two inputs - a hand and a
word (string). updateHand uses letters from the hand to spell the word, and then
returns a copy of the hand, containing only the letters remaining.
"""
def updateHand(hand, word):
    '''
    Assumes that 'hand' has all the letters in word. In other words, this assumes
    that however many times a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word and returns the
    new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    '''
    copiedHand = hand.copy()

    for char in word:
        copiedHand[char] = copiedHand.get(char, 0) - 1

    return copiedHand
