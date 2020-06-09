# set = {1, 2, 3}
# dic = {'Name': 'Anik', 10: 'Id'}
# print(type(set), type(dic))
# set = {}
# dt = {}
# list = []
# tuple = ()
# print(type(set), type(dt), type(list), type(tuple))
# # imposible
# # dic[{1, 2, 3}] = 'set'
# # dic[set] = {1, 2, 3}
# # print(dic)
# result = {'Ratul': 89, 'Ratan': 67, 'Nishat': 78}
# print('Result Of Ratan:', result['Ratan'])

result = {'Ratul': {'Bangla': 87, 'English': 89},
          'Ratan': {'Bangla': 74, 'English': 69},
          'Nishat': {'Bangla': 79, 'English': 91}}
print(result['Nishat']['English'])