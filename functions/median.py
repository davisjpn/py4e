def median (a,b,c):
    y.sort()
    middle = y[1]
    return middle
y = list()
x = input('Please input three numbers separated by a comma:')
xlist = list(x.split(","))
a = xlist[0]
b = xlist[1]
c = xlist[2]
a = int(a)
b = int(b)
c = int(c)
y.append(a)
y.append(b)
y.append(c)
print(median(a,b,c))
