"""
Problem 2: Paying Debt Off in a Year
15/15 Points

Write a program that calculates the minimum fixed monthly payment needed in
order to pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but
instead is a constant that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
    1. balance - the outstanding balance on the credit card
    2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will
pay off all debt in under 1 year.

Assume that the interest is compounded monthly according to the balance at
the end of the month (after the payment for that month is made). The
monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using this
payment scheme, which is okay.
"""
def payoffCalc(bal, air):
    '''
    bal: balance, positive int or float
    air: annual interest rate, as float

    returns: lowest fixed monthly payment required to pay off balance within
        12 months
    '''
    mthIntRate = air / 12.0    # monthly interest rate
    tempBal = bal    # balance var used for testing
    minMthPmt = 10    # minimum monthly payment
    paid = False    # var that states balance was paid off

    while paid == False:
        for i in range(12):
            tempBal -= minMthPmt    # min payment applied
            tempBal = tempBal + (mthIntRate * tempBal)    # balance with interest accrued
        if tempBal <= 0:
            paid = True
            break
        else:
            minMthPmt += 10
            tempBal = bal

    print("Lowest Payment: " + str(minMthPmt))
