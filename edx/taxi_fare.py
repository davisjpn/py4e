def fare (x):
    base_fare = 4.00
    meters = x * 1000
    if meters < 140:
        fare = base_fare
    else:
        fare = base_fare + (meters - 140) * .25
    return fare

x = input ('Please input the distance traveled in kilometers: ')
x = float(x)
print('$',"{0:,.2f}".format(fare(x)))
