x = 25
epsilon = 0.01
step = 0.07
guess = 4
while abs(guess**2-x) >= epsilon:
    print(guess)
    print(abs(guess**2-x))
    if guess <= x:
        guess += step
    else:
        break
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
