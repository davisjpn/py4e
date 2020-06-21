largest=None
count1 = 0
count = 0
condition = 0
while condition < 10:
    try:
        condition = condition + 1
        x = int(input('Please enter 10 integers separated by a comma:'))
        xlist = x.split(",")
        print(xlist)
        for item in xlist:
            if item.isnumeric():
                count1 = count1 + 1
            else:
                continue
        if count1 and len(xlist)==10:
            break
        else:
            print('Invalid input, please try again!')
            continue
    except:
        print('Invalid input, please try again')
        continue
for i in xlist:
    if int(i)%2 !=0:
        if largest == None:
            largest = int(i)
        elif int(i) > largest:
            largest = int(i)
    else:
        count = count + 1
if count == len(xlist):
    print('No odd number was entered')
else:
    print(largest,': was the largest negative number entered')
