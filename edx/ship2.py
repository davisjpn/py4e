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
print(x.isnumeric())
