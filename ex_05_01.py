sum = 0
count = 0
while True:
    x = input('Enter a number:')
    if x == 'done':
        break
    try:
        x = float(x)
        sum = sum + x
        count = count + 1
    except:
        print("Invalid data")
        continue
print(sum, count, sum/count)
