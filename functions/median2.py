def median (a,b,c):
    return a + b + c - max(a,b,c) - min(a,b,c)
condition = 0
xlist()
while condition > 5:
    try:
        condition = condition + 1
        x = input('Please input 3 numbers separated by a comma:')
        xlist = list(x.split(","))
        if xlist.isnumeric():
            break
        else:
            print('Invalid input. Please input whole numbers')
            continue
    except:
        print("Invalid input")
        continue
a = xlist[0]
a = int(a)
b = xlist[1]
b = int(b)
c = xlist[2]
c = int(c)
print(median(a,b,c))
