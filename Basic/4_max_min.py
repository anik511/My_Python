num1=int(input('Enter your first number: '))
num2=int(input('Enter your second number: '))
num3=int(input('Enter your third number: '))
if num1>num2 and num1>num3:
    print('Max:',num1)
    if num2>num3:
        print('Median:',num2,'\nMin:',num3)
    else:
        print('Median:',num3,'\nMin:',num2)
elif num2>num1 and num2>num3:
    print('Max:',num2)
    if num1>num3:
        print('Median:',num1,'\nMin:',num3)
    else:
        print('Median:',num3,'\nMin:',num1)
elif num3>num1 and num2<num3:
    print('Max:',num3)
    if num1>num2:
        print('Median:',num1,'\nMin:',num2)
    else:
        print('Median:',num2,'\nMin:',num1)
print('End of program')
