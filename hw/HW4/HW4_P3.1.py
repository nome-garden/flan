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