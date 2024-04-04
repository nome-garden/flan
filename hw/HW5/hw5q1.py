import numpy as np

#1 Hey Twin

def findEqual(n):
    #if all elements in each sublist are equal to the
    #iterated value (for loop?), concatenate that row to
    #a new array (np.concatenate(a,b))
    #np.searchsorted()
    newarr=np.empty(shape=[0,np.size(n[0])])

    for x in n:
    #     #print(x)
    #     for y in x:
    #         print(y)
    #         if y==x[0]:
                # np.append(newarr,y)
        if isRowEqual(x):
            print(x)
            newarr=np.append(newarr,[x], axis=0)
    return(newarr)

def isRowEqual(row):
    for num in row:
        if num!=row[0]:
            return False
    return True

arr = np.array([[1,1,1],[1,2,3],[3,3,3]])
print(findEqual(arr))

#shout out to jordan for the help!! he is so coded!!