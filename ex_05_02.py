largest = None
smallest = None
while True:
    x = input('Enter a number:')
    if x == 'done':
        break
    try:
        x = float(x)
        if largest is None:
            largest = x
        elif x > largest:
            largest = x
        if smallest is None:
            smallest = x
        elif x < smallest:
            smallest = x
    except:
        print("Invalid input")
        continue
print("Maximum is",largest)
print("Minimum is",smallest)
