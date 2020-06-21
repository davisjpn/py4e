print('Please think of a number between 0 and 100!')
low = 0
high = 100
while True:
    guess = (low + high)//2
    print('Is your secret number ' + str(guess) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the "\
    "quess is too low. Enter 'c' to indicate I quessed correctly. ")
    if ans == 'c':
        break
    elif ans == 'l':
        low = guess
    elif ans == 'h':
        high = guess
    else:
        print("Sorry, I did not understand your input.")
print('Game over. ' + 'Your secret number was: ' + str(guess))
