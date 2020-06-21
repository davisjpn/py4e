def isIN(string1,string2):
    count = 0
    for i in string1:
       for j in string2:
           if i == j:
               count = count + 1
    if count > 0:
        return True
    else:
        return False

def IsINN(string1, string2):
    return bool(string1 in string2 or string2 in string1)

x = input('Please enter string number 1:')
y = input('Please enter string number 2:')
#print (isIN(x,y))
print(IsINN(x,y))
