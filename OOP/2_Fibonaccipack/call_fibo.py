import fibo as fb
import trial

print("Call fibo from here!!")
x = int(input("Enter which Fibonacci number u want to see:"))

# n = fibo.fibonacci(x)

# it call aliasing {import fibo as fb}
a = fb.fibonacci(x)

# print('1st to', x, 'th Fibonacci numbers are:', n)

print('With aliasing 1st to', x, 'th Fibonacci numbers are:', a)

print('Name of imported module is', trial.__name__)
print('Name of the another imported module is', fb.__name__)
