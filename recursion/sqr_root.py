def sqrroot(n,g):
    if (10**-12 * -n)<=(n - g**2)<= (10**-12 * n):
        return g
    else:
        return sqrroot(n,(g + n/g)/2)

def main():
    n = int(input('Please input a number:'))
    g = int(input('Please input your guess:'))
    rec_sqr_root = sqrroot(n,g)
    print(rec_sqr_root)

main()
