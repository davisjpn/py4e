def fib(n):
    global fibCount
    if n == 0 or n == 1:
        return 1
    else:
        fibCount +=1
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))

fibCount = 0
x = int(input('Please enter the number of Fibonacci perids:'))
mainFib = x
fib(mainFib)

print('fib(2) was called', fibCount, 'times')

testFib(mainFib)
