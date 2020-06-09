strs = input("Enter A line:")
print(len(strs))
print(strs[1])
l = 1

for i in strs:
    if i == strs[len(strs)-l]:
        l += 1
        # print('Palindrome')
    else:
        print('Not Palindrome')
        break
    if l == len(strs):
        print('Palindrome')
        break
    else:
        continue
