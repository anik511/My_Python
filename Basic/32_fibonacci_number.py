def fibonacciOne(n, fib_zero, fib_first):
    for i in range(1, n + 1):
        fib_temp = fib_zero + fib_first
        fib_zero = fib_first
        fib_first = fib_temp
    print('Function 1', n, 'th fibonacci number is', fib_zero)


def fibonacciTwo(n, fib_zero, fib_first):
    for i in range(1, n + 1):
        fib_first, fib_zero = fib_zero + fib_first, fib_first
    print('Function 2', n, 'th fibonacci number is', fib_zero)


fib_zero = 0
fib_first = 1
nthNum = int(input("Enter a number:"))
fibonacciOne(nthNum, fib_zero, fib_first)
fibonacciTwo(nthNum, fib_zero, fib_first)
#
# import timeit
# t1 = timeit.timeit(fibonacciOne)
# t2 = timeit.timeit(fibonacciTwo)
# print(t1, t2, t1/t2)
# for i in range(1, nthNum+1):
#     fib_temp = fib_zero + fib_first
#     fib_zero = fib_first
#     fib_first = fib_temp
#     fib_first, fib_zero = fib_zero + fib_first, fib_first
