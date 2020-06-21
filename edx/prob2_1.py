balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthly_int_rate = annualInterestRate/12
#monthly_unpaid_balance = balance * (1 - monthlyPaymentRate)
#updated_balance = monthly_unpaid_balance + (monthly_int_rate * monthly_unpaid_balance)

for month in range(12):
    monthly_unpaid_balance = balance * (1 - monthlyPaymentRate)
    updated_balance = monthly_unpaid_balance + (monthly_int_rate * monthly_unpaid_balance)
    balance = updated_balance

print('Remaining balance:',round(balance,2))
