x = lambda a: a + 10
print('Sum:', x(10))
# multiple arguments to lambda function
z = lambda a, b: a + b
print('Sum:', z(20, 10))


def table(n):
    return lambda a: a * n


n = int(input())
b = table(n)
for i in range(1, 11):
    print(n, "x", i, '=', b(i))

lt = [1, 2, 3, 4, 10, 123, 22]
print(lt, type(lt))
oddlist = list(filter(lambda x: (x % 3 == 0), lt))
print(oddlist)

lts = [1, 2, 3, 4, 10, 123, 22]
new_list = list(map(lambda x: x * 3, lts))
print(new_list)
