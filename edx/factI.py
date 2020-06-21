def factI(n):
    """Assumes n an int>0
       Returns n!"""
    result=1
    while n > 1:
        result = result * n
        n -= 1
    return result
x = int(input('Please enter integer greater than 1:'))
print(factI(x))
