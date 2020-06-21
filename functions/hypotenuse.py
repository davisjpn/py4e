import string
import math
def hypotenuse(a,b):
    a_sqr = a**2
    b_sqr = b**2
    c_sqr = a_sqr + b_sqr
    c = math.sqrt(c_sqr)
    return c

a = input('Please enter side one of the triange:')
a = int(a)
b = input('Please enter side two of the triangle')
b = int(b)
print("{0:.2f}".format(hypotenuse(a,b)))
