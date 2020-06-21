def isInteger(s):
    if s.isdigit():
        return True
    else:
        if (s[0]== "+" or s[0]== "-") and (s[1:].isdigit()):
            return True
        else:
            return False
def main():
    s = input('Please input string:')
    s = s.strip()
    if s[0] == "+" or s[0] == "-":
        s = s[0] + s[1:].strip()
    if isInteger(s):
        print('That string represents an integer.')
    else:
        print('That string does not represent an integer.')

if __name__ == "__main__":
    main()
