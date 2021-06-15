#! python3
# Program to calculate the remaining credit card balance after one year if a person
# pays the minimum monthly payment

def Balance(balance, annualInterestRate, monthlyPaymentRate, month):
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    monthlyPaymentRate: minimum monthly payment rate as a decimal
    month: number of month after initial credit card statement

    returns credit card balance after number of months provided
    '''
    monthlyInterestRate = annualInterestRate/12.0
    monthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance + monthlyInterestRate*unpaidBalance
    if month == 1:
        return balance
    else:
        month -= 1
        return Balance(balance, annualInterestRate, monthlyPaymentRate, month)

remainingBalance = round(Balance(balance=5000, annualInterestRate=0.18, monthlyPaymentRate=0.02, month=12), 2)
print('Remaining balance: ', remainingBalance)