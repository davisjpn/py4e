def divisor(a,b):
    if b == 0:
        return a
    else:
        return divisor(b,(a%b))

def main():
    a = int(input('Please input first integer:'))
    b = int(input('Please input second integer:'))
    answer = divisor(a,b)
    print(answer)

main()
