import string
import json
import random
import urllib.request
count = 0
misses = 0
correct = 0
already_guessed = list()
guess_word = list()
initial = input('Please set the word size for your game? ')
size = int(initial)
start = input("How many incorrect 'guesses' are allowed? ")
trys = int(start)
url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words=json.loads(url.read())
random_word = random.choice(words)
while len(random_word) != size:
    random_word = random.choice(words)
print(random_word)
while misses < trys and correct != size:
    while True:
        guess = input ('Please guess a letter in the secret word ')
        guess = guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guess that letter. Choose again.')
        elif guess not in string.ascii_lowercase:
            print ('Please enter a letter')
        else:
            already_guessed.append(guess)
            break
    for letter in random_word:
        if guess == letter:
            correct = correct + 1
            guess_word.append(letter)
    if guess not in random_word:
            misses = misses + 1
            print('Sorry, your guess is incorrect')
            remaining = trys - misses
            remaining = str(remaining)
            print('You have ' + remaining +' incorrect guess(es) remaining')
if correct == size:
    print ('Congratulations, you correctly determined the secret word:', random_word)
else:
    print ('Your game is over, the secret word was:', random_word)
print(already_guessed)
print(guess_word)
#letters = string.ascii_lowercase
