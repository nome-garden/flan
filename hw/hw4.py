"2.1"
ls1 = list(range(51)) #stackoverflow https://stackoverflow.com/questions/29558007/how-can-i-generate-a-list-of-consecutive-numbers
print("2.1: ",ls1)

"2.2"
numeros = [2,4,6]
ls2=[]
def sq(n):
    return(n**2)

for numero in numeros:
    n = numero
    ls2.append(sq(n))
print(f"(2.2) tha numbers squared are: {ls2}") #with help from the debugging discussion! :D

"2.3"
lsA=list(range(1,11))
lsB=list(range(20,31))
lsC=[]

def odd(m):
    if m%2!=0:
        lsC.append(m)

for i in lsA:
    m=i
    odd(m)

for i in lsB:
    m=i
    odd(m)

print("lsA: ",lsA) #to check
print("lsB: ",lsB) #to check
print("(2.3) lsC: ", lsC)

#first when running, list showed as [1, None, 3, None, ...]
#second try, list showed as [1, (), 3, (), ...]
#fourth try I removed lsc.append(odd(m)) for each of the for i's, and added it instead to the if-statement and it works!!! :D

"3.1"
biglist = []
for i in range(0,5):
    n = []
    for j in range(1,6):
        n.append(j+5*i)
    biglist.append(n)
print("3.1: ",biglist)


#first try... the list has about a bajillion numbers... i am appending too much, there are too many duplicates!
#some try later, referring to https://snakify.org/en/lessons/two_dimensional_lists_arrays/, the numbers are correct but
#they aren't in list form nor separated by commas...
#had help from friend owen and https://stackoverflow.com/questions/35437028/understanding-creating-a-2d-list-with-nested-loops :D!

"3.2"
anotherlist=[]
for q in biglist:
    n=[]
    for r in q:
        if r%3==0:
            n.append("?")
        else:
            n.append(r)
    anotherlist.append(n)
print("3.2: ", anotherlist)

#thanks owen for suggestions and advice!!! :D

"4.1"
numlist = [1,1,2,3,4,4]
numlist2 = [5, 6, 8, 1, 8]
def removeDuplicates(x):
    x.sort()
    for num in numlist:
        if num==x[num]:
            x.remove(num)
    return x

removeDuplicates(numlist)
print("4.1 :",numlist)
removeDuplicates(numlist2)
print(numlist2)

#yasss did this all myself >:)
#actually doesn't work except for that very specific list :(
        