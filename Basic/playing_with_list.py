# 1
my_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# printing length of array/list
print(len(my_alphabet))
# using if-conditional statement that checks items
if len(my_alphabet) < 4:
    print('List has less then 4 items')


# 2
def check_func(nm, bl):
    if bl:
        print(nm, "called the function!!\n\n")


name = 'Anik Datta'

if 'Datta' in name:
    # calling check_func using two argument
    boolean = True
    check_func(name, boolean)

# 3
plants = ['Cactus', 'Alo-vera', 'Basil', 'Arrow-wood', 'Box-wood']
# printing each item and their index numbers
for plant in plants:
    print(plant, 'index number:', plants.index(plant))

# 4 Declaring and initializing array/list
wow_data_type = [] * 5
print(wow_data_type)
# using 6 data type instead of 5
wow_data_type = [3, 1.25, ['A', 'B'], {1, 2, 'Hi!!'}, True, 'String']
"""Here I found something interesting... 
if i change any index value(Without True) with 1(int).
The program will show you the index of True and 1 is same"""
print(wow_data_type, '\n')
# Iterating array/list
i = 0
while i < len(wow_data_type):
    if i + 1 != len(wow_data_type):
        temp = wow_data_type[i]
        wow_data_type[i] = wow_data_type[i + 1]
        wow_data_type[i + 1] = temp
    i += 2
print('After iteration:', wow_data_type, '\n')
# printing each item, index number and data type
for wow in wow_data_type:
    print(wow, 'index number:', wow_data_type.index(wow), 'Data Type:', type(wow))


print('\n')


# 5 printing each element of the array without loop
my_arr = [1, 2, 'One', True]
print("Printing Array/List without loop")
print(*my_arr, sep=', ')

# 6 Finding the common course
student_1_courses = ['Math', 'English', 'Programing']
student_2_courses = ['Geography', 'Spanish', 'Programing']
common = ''
for course in student_1_courses:
    for other in student_2_courses:
        if course == other:
            common += course
print('\n')
print("Common course:", common)
# More optimized way
common = str(set(student_1_courses).intersection(student_2_courses))
# converting list into set then set into string
common = common.replace("{'", "")
common = common.replace("'}", "")
print("Common course:", common)

# 7-8 same as 6
# 9
furniture = ['Table', 'Chairs ', 'Couch']
for word in furniture:
    print(word+":", *word)
    # for letter in word:
    #     print(letter)