# normal method

# making double of list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
NewLi = []
for x in li:
    NewLi.append(2*x)
print("New List:", NewLi)

# List Comprehension Method
Comprehension = [2 * x for x in li]
print("List Comprehension: ", Comprehension)

# Finding Even Numbers

# normal method
even = []
for x in li:
    if x % 2 == 0:
        even.append(x)
print('Normal Method Even Numbers:', even)

# List Comprehension Method
evenNmbr = [x for x in li if x % 2 == 0]
print("List Comprehension for Even Numbers: ", evenNmbr)

#Exr : sqr


# List Comprehension Method
sqr = [x * x for x in li]
print("List Comprehension ExR: ", sqr)
