def verse(n):
    print('On the '+ days.get(n)+' day of Christmas my true love sent to me')
    if n > 1:
        print(amounts.get(n) + ' ' + gifts[n-1])
    else:
        print('A partridge in a pear tree')
    return
def verses(n):
    if n > 1:
        print('On the '+ days.get(n)+ ' day of Christmas my true love sent to me')
        while n > 1:
            print(amounts.get(n) + ' ' + gifts[n-1]+ ',')
            n -=1
        print(gifts[0])
        print(' ')
        return
    else:
        print('On the '+ days.get(n)+ ' day of Christmas my true love sent to me')
        print('A partridge in a pear tree')
        return
gifts = ['and a partridge in a pear tree','turtles doves','french hens','calling birds',\
'golden rings','geese a laying','swans a swimming','maids a milking','ladies dancing',\
'lords of leaping','pipers piping','drummers drumming']
days = {1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth',7:'seventh',\
8:'eigth',9:'ninth',10:'tenth',11:'eleventh',12:'twelfth'}
amounts = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',\
8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}
numberofDays = len(gifts)
x = int(input('Please input what verse of the 12 Days of Christmas\
 you would like to see:'))
print('Here is the '+ days.get(x) + ' verse:')
print(' ')
verse(x)
print(' ')
print('Here is all ' + amounts.get(x) + ' verses:')
print(' ')
while x > 1:
    verses(x)
    x -=1
if x == 1:
    verse(x)
