Saarc = ['Bangladesh', 'India', 'Sri lanka', 'Pakistan', 'USA']
print(Saarc)

Saarc.append('Nepal')
Saarc.append('Afganistan')
#Not possible Saarc.append('Nepal', 'Afganistan')
print(Saarc)

Saarc.sort()
print('Sort',Saarc)

number = [9, 8, 7, 6, 3, 5, 2, 3, 1, 2, 5, 3, 1, 10]
print(number)

number.reverse()
print('Reverce',number)

number.sort()
print('Sort',number)

Saarc.reverse()
print('Reverce',Saarc)

number.reverse()
print('Reverce',number)

Saarc.insert(3, 'Bhutan')
print('Insert', Saarc)

Saarc.remove('Bhutan')
print('Remove', Saarc)

country = 'USA'
if country in Saarc:
    Saarc.remove(country)
    print('Removed:', country, 'From Saarc', Saarc)
else:
    print(country,'not in Saarc')

Saarc.append('Bhutan')
country = Saarc.pop()
print('Poped:', country)
print(Saarc)

country = Saarc.pop(1)
print('Poped with index:', country)

popedcountry = ['Bhutan', 'Pakistan']
Saarc.extend(popedcountry)
print('Another list Added:', Saarc)

print(number)
print('How many 3 we have in the list:', number.count(3))
print('How many 1 we have in the list:', number.count(1))

del(number[1])
print("Index 1 has been Deleted:", number)

# del(number)#number list will be deleted
# print('Number list:',number)

print(Saarc)
South =",".join(Saarc)
print(South)
South =" - ".join(Saarc)
print(South)