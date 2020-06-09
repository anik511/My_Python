def avg_list(list):
    avg = 0
    for i in list:
        avg +=i
    avg = avg/len(list)
    return avg
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = avg_list(list)
print('Average of list is:', r)