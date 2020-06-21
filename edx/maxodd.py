def maxodd(x,y,z):
    if x%2 != 0 and y%2 != 0 and z%2 !=0:
        if x>y and x>z:
            return print(x,':x is the largest odd number')
        elif y>x and y>z:
            return print(y,':y is the largest odd number')
        else:
            return print(z,':z is the largest odd number')
    elif x%2 and y%2:
        if x>y:
            return print(x,':x is the largest odd number')
        else:
            return print(y,':y is the largest odd number')
    elif y%2 and z%2:
        if y>z:
            return print(y,':y is the largest odd number')
        else:
            return print(z,':z is the largest odd number')
    elif x%2 and z%2:
        if x > z:
            return print(x,':x is the largest odd number')
        else:
            return print(z,':z is the largest odd number')
    else:
        if x%2: return print(x,':x is the largest odd number')
        if y%2: return print(y,':y is the largest odd number')
        if z%2: return print(z,':z is the largest odd number')
x = input('Please input three numbers, separated by a comma:')
xlist = x.split(",")
x = xlist[0]
x = int(x)
y = xlist[1]
y = int(y)
z = xlist[2]
z = int(z)
maxodd(x,y,z)
