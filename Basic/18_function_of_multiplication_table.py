def multiplicationTable(n):
    for i in range(1,11):
        print(n, 'x', i, '=', n*i)
n = int(input('Enter a numbr for Multiplication Table:'))
multiplicationTable(n)