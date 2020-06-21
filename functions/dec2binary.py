binary = ""
x = int(input('Please input an integer:'))
q = x
if q == 0:
    binary = 0
    print('The binary equivalent of ' + str(x) + ' is ' + str(binary))
else:
    while q > 0:
        r = q%2
        binary = str(r) + binary
        q = int(q/2)
    print('The binary equivalent of ' + str(x) + ' is ' + str(binary))
