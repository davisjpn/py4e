balance = 320000
int_rate = 0.2
monthly_int_rate = int_rate/12
monthly_pmt_lb = balance/12
monthly_pmt_ub = (balance * (1 + monthly_int_rate)**12)/12
originalbalance = balance
while abs(balance) > .02:
    balance = originalbalance
    payment = (monthly_pmt_ub - monthly_pmt_lb)/2 + monthly_pmt_lb
    for month in range(12):
        balance -= payment
        balance *= (1 + monthly_int_rate)
    if balance > 0:
        monthly_pmt_lb = payment
    else:
        monthly_pmt_ub = payment
print(balance)
print('Lowest payment: ', round(payment, 2))
