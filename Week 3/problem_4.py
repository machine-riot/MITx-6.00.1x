"""
Problem 4: The Game
15/15 Points

Now you will implement the function hangman, which takes one parameter - the
secretWord the user is to guess. This starts up an interactive game of Hangman
between the user and the computer.
"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word of the game

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many letters the
      secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess about
      whether their guess appears in the computers word.

    * After each round, you should also display to the user the partially
      guessed word so far, as well as the letters that the user has not yet
      guessed.
    '''
    guess = ''
    guessesLeft = 8
    lettersGuessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")

    # main Hangman loop
    while guessesLeft > 0:
        print("-------------")
        print("You have " + str(guessesLeft) + " guesses left")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed += guess
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("-------------")
                return print("Congratulations, you won!")
                break
        elif guess not in secretWord:
            lettersGuessed += guess
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
            if guessesLeft == 0:
                print("-------------")
                return print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        elif guess == ' ':
            break
