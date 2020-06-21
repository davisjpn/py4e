def is_palindrome(x):
    if len(x) <=1:
        return True
    else:
        return x[0] == x[len(x)-1] and is_palindrome(x[1 : len(x) - 1])

def main():
    x = input('Please input string:')
    if is_palindrome(x):
        print('String is a palindrome')
    else:
        print('String was not a palindrome')

main()
