def chkpass(s):
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    if len(s) > 7:
        test1 = True
    if any(i.isupper() for i in s):
        test2 = True
    if any(i.islower() for i in s):
        test3 = True
    if any(i.isnumeric() for i in s):
        test4 = True
    if test1 == True and test2 == True and test3 == True and test4 == True:
        return True
    else:
        return False

s = input('Please input password:')
print(chkpass(s))
