exit = 'Go'
def add(a,b):
    return a+b
while True:
    if exit == 'Exit':
        break
    elif exit == 'Go':
        n1 = int(input('Enter a number:'))
        n2 = int(input('Enter another number:'))
        result = add(n1, n2)
        print('Result is:', result)
        exit = input('Enter Exit to quit or enter Go to Perform operation:')
print('Program ends')
