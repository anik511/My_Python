strs = input("Enter A line:")
# print(type(strs))
# uppers = [l for l in strs if l.isupper()]
# lower = [l for l in strs if l.islower()]

# numbers = [l for l in strs if l.isdigit()]
# print ("".join(uppers))
# print ("".join(lower))
# print ("".join(numbers))


numbers = ""
uppers = ""
lower = ""
anything = ""
for l in strs:
    if l.isdigit():
        numbers += l
    elif l.isupper():
        uppers += l
    elif l.islower():
        lower += l
    else:
        anything += l
print(numbers,"\n",uppers,"\n",lower,"\n",anything)