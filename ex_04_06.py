def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        pay = ((h - 40) * r * 1.5) + (40 * r)
    return pay
a = input("Enter hours:")
b = input("Enter rate:")
a = float(a)
b = float(b)
x = computepay(a, b)
print("Pay",x)
