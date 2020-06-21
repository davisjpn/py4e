x = int(input('Please enter integer from which to calculate its cube root:'))
epsilon = 0.01
numGuesses = 0
low = min(x, 0)
high = max(1.0, x)
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:
    print('low = ', low, 'high =', high, 'ans=', ans)
    numGuesses +=1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)
