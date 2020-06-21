def bisection(a,b):
    low = a
    high = b
    mid = (low + high)/2

    if number == mid:
        return 'Your number is: ' + str(number)
    else:
        if number < mid:
            return bisection(low, mid)
        if number > mid:
            return bisection(mid, high)

number = int(input('Please guess a number between 0 and 100: '))
answer = bisection(0,100)
print(answer)
