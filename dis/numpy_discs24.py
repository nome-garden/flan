import numpy as np
import time

def function(num):
    return num**2

def loop_speedtest(n):
    start = time.time() #measures time when we start
    result = list(range(n)) #makes a list from 1 to n
    for i in result:
        result[i] = function(result[i]) #for every element in result, we apply function to it
    end = time.time() #define end time
    return end - start #return difference

def numpy_speedtest(n):
    start = time.time()
    result = np.arange(n) #doing the same thing as above function
    result = function(result) #applys function to every element of array
    end = time.time()
    return end - start

reps = 10000
print(loop_speedtest(reps))
print(numpy_speedtest(reps))
#the number that results is an indicator of your computer's speed? So the lower the better!


##
## Find the unique elements in an array and 
# the number of each element
## [10,2,5,10,8,2,9,8]
## [2,5,8,9,10], [2,1,2,1,2]
## 
## write a function that returns list of unique elements, and a list of non-unique numbers

myArray = np.array([10,2,5,10,8,2,9,8])

print(np.unique(myArray,return_counts = True)) 
#print(np.unique(myArray)) will return array of unique elems
#return_counts=True creates another array that indicates the number of occurences
#of the corresponding element 

## Given a 2D array, find the mean of each of the 
## columns and replace each element less than the 
## column's mean with the mean

##([[34,37,29],  
## [1, 36, 41],
## [37,34,29],
## [1, 49, 14]])

myArray = np.array([[34,37,29],[1, 36, 41],[37,34,29], [1, 49, 14]])
means = np.mean(myArray, axis = 0) #axis parameter allows us to choose what dimension to operate on?? 
#axis 0 calculates mean for each  row,  1 is columns?
for i in range(myArray.shape[1]):
    myArray[:,i][myArray[:,i] < means[i]] = means[i]
    ##array[Boolean Expression] = stuff
    ##Is the same as 
    ##for i in range(len(array)):
    ## if boolean expression:
    ##    array[i] = stuff


print(myArray)
