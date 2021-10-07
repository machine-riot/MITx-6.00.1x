"""
Problem 3: CiphertextMessage
15/15 Points

Given an encrypted message, if you know the shift used to encode the message,
decoding it is trivial. If message is the encrypted message, and s is the shift
used to encrypt the message, then apply_shift(message, 26-s) gives you the
original plaintext message.

The problem, of course, is that you don't know the shift. But our encryption
method has only 26 distinct possible values for the shift! We know English is
the main language of these emails, so if we can write a program that tries
each shift and maximizes the number of English words in the decoded message, we
can decrypt their cipher! A simple indication of whether or not the correct
shift has been found is if most of the words obtained after a shift are valid
words.

Fill in the methods of the class CiphertextMessage according to the
specifications in ps6py.
"""
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shiftTuple = ()
        shiftedMsg = ''
        bestShift = 0
        valid = 0
        priorValid = 0

        for i in range(26):
            shiftedMsg = self.message_text
            shiftedMsg = self.apply_shift(i)
            shiftedMsg = shiftedMsg.split(' ')
            for word in shiftedMsg:
                if is_word(self.valid_words, word):
                    valid += 1
            if valid > priorValid:
                shiftTuple = (i,)
                bestShift = i
            priorValid = valid
            valid = 0

        shiftedMsg = self.apply_shift(bestShift)
        shiftTuple += (shiftedMsg,)
        return shiftTuple
