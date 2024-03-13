"4.1"
numlist = [1,1,2,3,4,4]
numlist2 = [5, 6, 8, 1, 8]
def removeDuplicates(x):
    x.sort()
    for num in numlist:
        if num==numlist[num]:
            numlist.remove(num)

removeDuplicates(numlist)
print("4.1 :",numlist)
removeDuplicates(numlist2)
print(numlist2)

#yasss did this all myself >:)
#actually doesn't work except for that very specific list :(