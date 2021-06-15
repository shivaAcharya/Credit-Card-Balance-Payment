#! python3
# Program to calculate the lowest monthly fixed payment amount which will pay off a credit
# card balance within 12 months.

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0

# Create low and high bounds for Bisection Search
low = balance/12.0
high = balance*(1 + monthlyInterestRate)**12

newbalance = balance

while abs(newbalance) > 0.06:
    newbalance = balance
    monthlyPayment = round((high + low)/2, 2)
    for i in range(12):
        monthlyUnpaidBalance = newbalance - monthlyPayment
        newbalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
        
    # Update low or high bounds based on newbalance result
    if newbalance > 0:
        low = monthlyPayment
    else:
        high = monthlyPayment
print('Lowest Payment: ', monthlyPayment)