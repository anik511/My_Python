# li = [11, 3, 22, 65, 3, 1, 9, 21]
# print(li)
# li.sort()
# print('Sort', li)
# li.reverse()
# print('Reverse', li)
# li.append(65)
# print('Append', li)
# li.insert(1,100)
# print('Insert', li)
# li.pop()
# print('Pop', li)
# li.remove(100)
# print('Remove', li)
# li2 = ['anik', 'Python']
# print(li2)
# li.extend(li2)
# print('Extend', li)
# print('Count', li.count(3))
#
# # Problem in copy method
# # li2.copy()
# # print('li2 Copy', li2)
#
#
# li.clear()
# print('Clear', li)

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    word = list(word)
    word.sort()
    x = ord(word[len(word) - 1]) - ord(word[0]) + 1
    h = h[0:x]
    h.sort()
    return h[len(h) - 1] * len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
