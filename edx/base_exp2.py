def iterPower(base,exp):
    amount = 1
    if exp == 0:
        return 1
    else:
        while exp > 0:
            amount *= base
            exp -= 1
        return amount
print(iterPower(2,3))
