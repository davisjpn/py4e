x = int(input('Please enter an integer:'))
x = abs(x)
root = x
pwr = 2
count = 0
check = 4 * (x*2+1)

while pwr > 1 and pwr < 6:
    while abs(root) <= x:
        if root**pwr == x:
            print('The root is ' + str(root) + ' and the power is ' + str(pwr))
        else:
            count = count + 1
        root-=1
    pwr+=1
    root = x
if count == check:
    print('There are not such pair of integers for' + str(root))
