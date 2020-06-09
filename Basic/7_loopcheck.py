r=0
n=1
for i in range (50):
    r+=n
    n+=1
print('Test One:',r)

re=0
for i in range (51):#i start count from 0
    re+=i
print('Test Two:',re)

res=0
for i in range (1,51):#i start count from 1
    res+=i
print('Test Three:',re)

#increasing by 5
for i in range(0,50,5):
    print(i)

#max min by loop... array
arr = [7,32,4,5,1,9,0,7,98,3,5]
max_n = arr[0]
for x in arr:
    print('loop:',x)
    if x> max_n:
        print('Change:',x)
        max_n=x
print('Max:',max_n)
