#6 min and max w loops

#maxes
list1=[1,2,3,4]

max1=list1[0]

for num in list1: #for loop
    if num>max1:
        max1=num
#referenced from favtutor
print(max1)

list2=[5,6,7,8]
max2=list2[0]

y=len(list2)-1
while y>-1: #while loop
    if list2[y]>max2:
        max2=list2[y]
    y-=1

print(max2)

#mins
min1=list1[0]

for num in list1: #for loop
    if num<min1:
        min1=num
#referenced from favtutor
print(min1)

min2=list2[0]

y=len(list2)-1
while y>-1: #while loop
    if list2[y]<min2:
        min2=list2[y]
    y-=1

print(min2)