tarminate=False
while not tarminate:
    num1=int(input('Enter a number: '))
    num2=int(input('Enter another number: '))
    while True:
        operation=input('Please enter add/sub or quit for exit: ')
        if operation=='quit':
            terminate=True
            break
        elif operation not in ['add','sub']:
            print('Unknown Operation!')
            continue
        elif operation=='add':
            print('Result of add is: ',num1+num2)
            break
        elif operation=='sub':
            print('Result of sub is: ',num1-num2)
            break
print('Program Ends')
