def shipping(x):
    base_rate = 10.95
    count = 0
    if x >1:
        count = x - 1
    else:
        count = 0
    cost = base_rate + count * 2.95
    return cost
condition = 0
while condition < 10:
    try:
        condition = condition + 1
        x =(input('Please enter the number of items to be shipped:'))
        if x.isnumeric() and int(x)>0:
            break
        else:
            print('Please enter a positive whole number')
            continue
    except:
        continue
x = int(x)
print(shipping(x))
