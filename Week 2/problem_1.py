"""
Problem 1: Paying Debt off in a Year
10/10 Points

Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each
month.

The following variables contain the values described below:
    1. balance - the outstanding balance on the credit card
    2. annualInterestRate - annual interest rate as a decimal
    3. monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure
to print out no more than two decimal digits of accuracy.
"""
def minPaymentCalc(bal, air, mpr):
    '''
    bal: balance, positive int or float
    air: annual interest rate, as float
    mpr: monthly payment rate, minimum payment as float

    returns: remaining balance at the end of a year
    '''
    mthIntRate = air / 12.0    # monthly interest rate

    for i in range(12):
        minMthPmt = mpr * bal    # minimum monthly payment
        bal -= minMthPmt    # min payment applied
        bal = bal + (mthIntRate * bal)    # balance with interest accrued

    print("Remaining balance: " + str(round(bal, 2)))
