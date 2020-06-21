k = int(input('Please input integer for which to find its cube root:'))
epsilon = 0.01
guess = k/2
while abs(guess * guess -k) >= epsilon:
    guess = guess - (((guess**3)-k)/(3*guess**2))
print('Cube root of', k, 'is about', guess)
