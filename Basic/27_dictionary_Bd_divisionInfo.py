bd_division_info = {}
bd_division_info['Dhaka'] = {'District': 13, 'Upazila': 93, 'Union': 1833}
bd_division_info['Barisal'] = {'District': 6, 'Upazila': 39, 'Union': 333}
bd_division_info['Chittagong'] = {'District': 11, 'Upazila': 97, 'Union': 336}
bd_division_info['Khulna'] = {'District': 10, 'Upazila': 59, 'Union': 270}
bd_division_info['Mymensingh'] = {'District': 4, 'Upazila': 34, 'Union': 350}
bd_division_info['Rajshahi'] = {'District': 8, 'Upazila': 70, 'Union': 508}
bd_division_info['Rangpur'] = {'District': 8, 'Upazila': 58, 'Union': 536}
bd_division_info['Sylhet'] = {'District': 4, 'Upazila': 38, 'Union': 334}
print(bd_division_info)
for key in bd_division_info:
    print(key)
# point 1
print('Point 1')
for key in bd_division_info:
    print(key)
    print(bd_division_info[key])
# point 2
print('Point 2')
for key, val in bd_division_info.items():
    print(key)
    print(val)

Divisions = bd_division_info.keys()
print(Divisions)
for div in Divisions:
    print('Division', div)

for div in Divisions:
    print(div, 'Upazilas:', bd_division_info[div]['Upazila'])

# all details
for div in Divisions:
    print(div, 'Districts:', bd_division_info[div]['District'], 'Upazilas:', bd_division_info[div]['Upazila'], 'Unions:',bd_division_info[div]['Union'])
