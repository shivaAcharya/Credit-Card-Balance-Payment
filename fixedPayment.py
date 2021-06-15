#! python3
# Program to calculate a lowest monthly fixed payment amount (in 10s) which will pay off a credit
# card balance within 12 months.

balance = 3769
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 0
newbalance = balance
while newbalance > 1:
    monthlyPayment += 10
    newbalance = balance
    for i in range(12): # Looping for 12 months
        monthlyUnpaidBalance = newbalance - monthlyPayment
        newbalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
print('Lowest Payment: ', monthlyPayment)