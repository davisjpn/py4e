def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    aStr = aStr.replace(" ","")
    low = aStr[0]
    high = aStr[-1]
    mid = aStr[len(aStr[aStr.index(low):aStr.index(high)])+1//2]
    print(len(aStr))
    print(char)
    print(aStr)
    print(mid)
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr[0]
    elif char == mid:
        return True
    elif char < mid:
        return isIn(char,aStr[aStr.index(low):aStr.index(mid)])
    else:
        return isIn(char,aStr[aStr.index(mid):aStr.index(high)])


print(isIn('c','abcdefg'))
