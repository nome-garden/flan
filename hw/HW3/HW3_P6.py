#6 min and max w loops
#i put them in function form but i don't know why it doesn't work :(

#maxes
list1=[1,2,3,4]
max1=""
def formax(n):
    max1=n[0]
    for num in n: #for loop
        if num>max1:
            max1=num
    return(max1)
#referenced from stackoverflow
print(formax(list1))

list2=[5,6,7,8]
max2=""
def whilemax(n):
    max2=n[0]
    y=len(n)-1
    while y>-1: #while loop
        if n[y]>max2:
          max2=n[y]
    y-=1
    return(max2)

print(whilemax(list2))

#mins
min1=""
def formin(n):
    min1=n[0]
    for num in n: #for loop
        if num<min1:
            min1=num
    return(min1)
#referenced from stackoverflow
print(formin(list1))

min2=""
def whilemin(n):
    min2=n[0]
    y=len(n)-1
    while y>-1: #while loop
        if n[y]<min2:
            min2=n[y]
        y-=1
    return(min2)

print(whilemin(list2))