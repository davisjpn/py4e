import string
import json
import random
import urllib.request
count = 0
misses = 0
correct = 0
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
    guess = input ('Please guess a letter in the secret word ')
    for letter in random_word:
        if guess == letter:
            correct = correct + 1
    if guess not in random_word:
            misses = misses + 1
if correct == size:
    print ('Congratulations, you correctly determined the secret word:', random_word)
else:
    print ('Sorry you are out of guesses, the secret word was:', random_word)
#letters = string.ascii_lowercase
