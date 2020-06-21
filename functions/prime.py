def prime(x):
    count = 0
    s = x
    while s > 0:
        if x%s == 0:
            count = count+1
        s -= 1
    if count == 2:
        return  str(x) + ' is a Prime number'
    else:
        return  str(x) + ' is not a Prime number'
def main():
    x = int(input('Please input a postive integer greater than zero:'))
    print(prime(x))

main()
