strs = input("Enter A line:")
print(type(strs))
# strs = strs.split()
# print(type(strs))
new = ''
print(strs)
n = 0
while n < len(strs):
    if n + 1 <len(strs):
        new += strs[n + 1]
        new += strs[n]
    n += 2
print(new)