def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    aStr = aStr.replace(" ","")
    low = 0
    high = len(aStr) - 1
    mid = (low + high)//2
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr[low]
    elif len(aStr) == 2:
        return char == aStr[low] or char == aStr[1]
    elif char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char,aStr[(low):(mid+1)])
    else:
        return isIn(char,aStr[(mid):(high+1)])

print(isIn('c','abdefg'))
