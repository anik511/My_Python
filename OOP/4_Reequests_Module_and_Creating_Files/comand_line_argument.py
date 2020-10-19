import sys

print(sys.argv)
print(type(sys.argv))
arguments = sys.argv
a = arguments[1]
b = arguments[2]
print(int(a) + int(b))
