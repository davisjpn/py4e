def bin(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return str(bin(x//2)) + str(x%2)

def main():
    x = int(input('Please input a non-negative integer:'))
    binary = bin(x)
    print(binary)

main()
