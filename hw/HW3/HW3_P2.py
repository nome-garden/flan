#2 min and max

list1=[14,55,62,8,11]
max=""
min=""

def mm():
    eval(input(list1)) #referenced from favtutor

max=list1[0]
min=list1[0]

for num in list1:
    if num>max:
        max=num
    if num<min:
        min=num


print(max)
print(min)
tuple=(min,max)
print(tuple)