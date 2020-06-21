import math
def polygon(n,s):
    """ two input variables: n (number of sides) and s (length of sides)for
    a regular polygon. the function will return the sum of the area and square of the
    perimeter of the regular polygon. """
    area = (0.25 * n * s**2)/(math.tan(math.pi/n))
    perimeter = n * s
    return round(area + perimeter**2,4)

print(polygon(8,5))
