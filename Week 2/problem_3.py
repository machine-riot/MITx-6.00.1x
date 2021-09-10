"""
Problem 3: Using Bisection Search to Make the Program Faster
20/20 Points

Calculate a more accurate fixed monthly payment than Problem 2 using bisection
search.

The following variables contain values as described below:
    1. balance - the outstanding balance on the credit card
    2. annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such
that we can pay off the entire balance within a year.
"""
def payoffCalcBisection(bal, air):
    '''
    bal: balance, positive int or float
    air: annual interest rate, as float

    returns: lowest fixed monthly payment required to pay off balance within
        12 months
    '''
    mthIntRate = air / 12.0    # monthly interest rate
    tempBal = bal    # balance var used for testing
    epsilon = 0.01
    lower = bal / 12
    upper = (bal * (1 + mthIntRate)**12) / 12.0

    while tempBal > epsilon or tempBal < -epsilon:
        mthPmt = (lower + upper) / 2    # monthly payment
        for i in range(12):
            tempBal -= mthPmt    # min payment applied
            tempBal = tempBal + (mthIntRate * tempBal)    # balance with interest accrued
        if tempBal <= 0:
            upper = mthPmt
            tempBal = bal
        else:
            lower = mthPmt
            tempBal = bal

    print("Lowest Payment: " + str(mthPmt))
