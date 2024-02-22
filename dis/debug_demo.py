def add(x,y):
    """
    >>> add(2, 3)
    5
    >>> add(1,5)
    6
    """
    return(x+y)
    print(add(5,6))

def factLoop(n):
    """
    >>> factLoop(3)
    6
    """
    total=1
    for i in range(1,n+1):
        total*=i
    return total

print(factLoop(3))