import numpy as np

#1 Hey Twin

arr = np.array([[1,1,1],[1,2,3],[3,3,3]])
def findEqual(n):
    #if all elements in each sublist are equal to the
    #iterated value (for loop?), concatenate that row to
    #a new array (np.concatenate(a,b))
    #np.searchsorted()
    newarr=np.array([])
    for x in n:
    #     #print(x)
    #     for y in x:
    #         print(y)
    #         if y==x[0]:
                # np.append(newarr,y)
        if isRowEqual(x):
            print(x)
            newarr=np.append(newarr,x)
    return(newarr)

def isRowEqual(row):
    for num in row:
        if num!=row[0]:
            return False
    return True

print(findEqual(arr))
