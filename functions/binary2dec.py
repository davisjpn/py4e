x = (input('Please enter a binary number:'))
s = len(x)
total = 0
for char in range(0,s):
    r = int(x[char]) * 2 ** (s-1-char)
    total = r + total
print('The decimal equivalent to the binary number '+ x +' is '+ str(total))
