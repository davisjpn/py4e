import string
import json
import random
import time
import urllib.request
count = 0
misses = 0
correct = 0
already_guessed = list()
initial = input('Please set the word size for your game? ')
size = int(initial)
start = input("How many incorrect 'guesses' are allowed? ")
trys = int(start)
guess_word = ['_'] * size
print ('Please wait a moment for the game to begin....')
url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words=json.loads(url.read())
random_word = random.choice(words)
while len(random_word) != size:
    random_word = random.choice(words)
#print(random_word)
print ("Let's begin, your hangman is "+ initial + ' letters long', guess_word)
while misses < trys and correct != size:
    while True:
        time.sleep(.5)
        if correct or misses !=0:
            print("Here's a breakdown of your successful guesses so far  ", guess_word)
            time.sleep(.5)
        guess = input ('Please guess a letter in the secret word ')
        guess = guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guess that letter.')
            print("Here's a list of all your quesses, so far", already_guessed)
            time.sleep(.5)
            print('Chose a different letter at the next prompt.')
        elif guess not in string.ascii_lowercase:
            print ('Please enter a letter')
        else:
            already_guessed.append(guess)
            break
    if guess in random_word:
        correct = correct + 1
        n = size
        while n >= 0:
            if guess==random_word[n-1]: guess_word[n-1] = guess
            n = n-1
    if guess not in random_word:
            misses = misses + 1
            print('Sorry, your guess is incorrect')
            remaining = trys - misses
            remaining = str(remaining)
            print('You have ' + remaining +' incorrect guess(es) remaining')
            print("Here's a list of all your guesses, so far ", already_guessed)
if correct == size:
    print ('Congratulations!, you correctly determined the secret word:', random_word)
else:
    print ('Your game is over, the secret word was:', random_word)
