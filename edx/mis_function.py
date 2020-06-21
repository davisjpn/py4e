def a(x, y, z):
    if x:
        return y
    else:
        return z
print(type(a))
print(a(False, 2, 3))
