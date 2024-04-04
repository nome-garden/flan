#2 Checkers
import numpy as np

arr = np.zeros((8,8),dtype=int)

def checkerboard(x):
    x[1::2,::2] = 1 # (odd_rows, even_columns)
    x[::2,1::2] = 1 # (even_rows, odd_columns)
    return(x)

#credit to priya_03 and demokritos on stackoverflow
#https://stackoverflow.com/questions/2169478/how-to-make-a-checkerboard-in-numpy


print(checkerboard(arr))
print(checkerboard(arr).shape)

#FAILED ATTEMPT IN PROGRESS:  :(
#a = np.array([1,0,1,0,1,0,1,0])
#b=np.expand_dims(a,axis=1)
#print(np.shape(a))
#print(b) 
    