balance = 4473
original_balance = balance
annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
monthlypayment = 10
monthly_int_rate = annualInterestRate/12
count = 0
#monthly_unpaid_balance = balance * (1 - monthlyPaymentRate)
#updated_balance = monthly_unpaid_balance + (monthly_int_rate * monthly_unpaid_balance)
while True and count < 100:
    for month in range(12):
        monthly_unpaid_balance = balance - monthlypayment
        updated_balance = monthly_unpaid_balance + (monthly_int_rate * monthly_unpaid_balance)
        balance = updated_balance
    if balance <= 0:
        break
    else:
        balance = original_balance
        monthlypayment += 10
    count += 1

print('Lowest Payment:',round(monthlypayment,0))
