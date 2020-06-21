def factR(n):
    """Assumes n an int > 0
       Returns n!"""
    if n == 1:
        return n
    else:
        return n*factR(n-1)
x = int(input('Please enter positive integer:'))
print(factR(x))
