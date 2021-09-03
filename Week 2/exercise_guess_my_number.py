"""
Exercise: Guess My Number
10/10 Points

You (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number.

For example:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
too low. Enter 'c' to indicate I guessed correctly.
...
...
...
Game over. Your secret number was: 83

Note: your program should use input to obtain the user's input! Be sure to handle
the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the user
explaining you did not understand the input. Then, you should re-ask the
question, and prompt again for input.
"""
high = 100
low = 0
guess = 0
guess_track = ''

print("Please think of a number between 0 and 100!")
while guess_track != 'c':
    guess = (high + low)//2
    print("Is your secret number " + str(guess) + "?")
    guess_track = input("Enter 'h' to indicate the guess is too high. enter 'l' to \
    indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess_track == 'h':
        high = guess
    elif guess_track == 'l':
        low = guess
    elif guess_track == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
