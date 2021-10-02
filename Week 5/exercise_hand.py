"""
Exercise: hand
5/5 Points

In this problem, you'll be asked to read through an object-oriented
implementation of the hand from the word game problem of Problem Set 4. You'll
then be asked to implement one of its methods. Note that the implementation of
the object-oriented version of the hand is a bit different than how we did
things with the functional implementation; pay close attention to doc strings
and read through the implementation carefully.
"""
class hand(object):
    def __init__(self):

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output
