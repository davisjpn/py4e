x = input('Please input string:')
s = len(x)
l = x[ ::-1]
r = -s
count = 0
while s > 0:
    if x[(-r-s)] == l[(0-s)]:
        count = count+1
    else:
        print('The string is not a palindrome.')
        break
    s -= 1
if count == len(x):
    print('The string is a palindrome.')
