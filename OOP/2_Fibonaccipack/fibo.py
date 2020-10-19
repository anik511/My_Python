def fibonacci(n):
    fib_zero = 0
    fib_first = 1
    li = []
    for i in range(1, n + 1):
        fib_first, fib_zero = fib_zero + fib_first, fib_first
        li.append(fib_zero)
    return li


# print('Out of if statement', fibonacci(10))


if __name__ == '__main__':
    print(fibonacci(10))
