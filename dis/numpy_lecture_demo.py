"""
if there is a problem with this line:
    do Command+shift+p or Ctrl+shift+p
    search Python: Select Interpreter
    select the 'base' or conda environment
"""
import numpy as np

# add two arrays and add two lists
ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = ls1 + ls2
print(ls3)
print(f'adding two lists: {ls1+ls2}') #adding two lists; two ways

arr1 = np.array([1,2,3]) #initializing an array
arr2 = np.array([4,5,6])
arr3 = arr1 + arr2
print(arr3)
print(f'adding two arrays: {arr1+arr2}') #adding arrays is the same with adding lists

# sum of numbers

def loopSum():
    """
    Takes the sum of the numbers 0 to 100 with a loop
    """
    sum = 0
    for i in range(101):
        sum += i
    return(sum)

def arraySum():
    """
    Takes the sum of the numbers 0 to 100 user Numpy
    """
    return np.sum(np.arange(101))

# slicing

def lastTwo(myarr):
    """
    Returns the last two columns of the array
    Try to make it work for any input array!
    >>> arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    >>> lastTwo(arr)
    array([[2, 3],
           [5, 6],
           [8, 9]])
    """
    return "YOUR CODE HERE"

def everyOther(way, myarr):
    """
    Returns every other row or column depending on input for way
    >>> arr = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
    >>> everyOther("row", arr)
    array([[1, 2, 3],
           [7, 8, 9]])
    >>> everyOther("column", arr)
    array([[1, 3],
           [4, 6],
           [7, 9]])
    """
    if way == 'row':
        return "YOUR CODE HERE" 
    elif way == 'column':
        return "YOUR CODE HERE"
    else:
        return "YOUR CODE HERE" 

# useful functions

# only do this if time permits

print(f'I can make an array of zeros: {np.zeros(4)}')
print(f'I can make an array of random numbers: {np.random.random(5)}')
