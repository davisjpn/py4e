import random
import string

def rnumber():
    y = random.choice(range(7,11))
    list =[]
    count = 0
    while count < y:
        x = chr(random.choice(range(33,127)))
        list.append(x)
        count += 1
    return print(*list,sep='')

def main():
    rnumber()

main()
