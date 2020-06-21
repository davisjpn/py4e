balance = 999999
original_balance = balance
annualInterestRate = 0.18
monthly_int_rate = annualInterestRate/12
monthlypayment_low = balance/12
monthlypayment_high = (balance * (1 + monthly_int_rate)**12)/12
mid = (monthlypayment_low + monthlypayment_high)/2
count = 0
while True:
    for month in range(12):
        monthly_unpaid_balance = balance - mid
        updated_balance = monthly_unpaid_balance + (monthly_int_rate * monthly_unpaid_balance)
        balance = updated_balance
    print(balance)
    print(mid)
    if abs(balance - 0)< .05:
        break
    elif balance > 0 :
        monthlypayment_low = mid
        mid = (monthlypayment_low + monthlypayment_high)/2
        balance = original_balance
    else:
        monthlypayment_high = mid
        mid = (monthlypayment_low + monthlypayment_high)/2
        balance = original_balance
print('Lowest Payment:',round(mid,0))
