print('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = int((low + high)//2)
ans = ""
while ans != 't':
    print('Is your secret number ' + str(guess) + '? ')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the "\
    "quess is too low. Enter 'c' to indicate I quessed correctly. ",end='')
    ans = input()
    while (ans != 'h') and (ans != 'l') and (ans != 'c'):
        print('Sorry, I did not understand your input.')
        print('Is your secret number ' + str(guess) + '? ')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the "\
        "quess is too low. Enter 'c' to indicate I quessed correctly. ",end='')
        ans = input()
    if ans == 'c':
        break
    elif ans == 'l':
        low = guess
    else:
        high = guess
    guess = int((low + high)//2)
print('Game over. ' + 'Your secret number was: ' + str(guess))
