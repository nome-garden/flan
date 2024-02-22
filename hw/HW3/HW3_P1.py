#1 power of a number
def exp(x,y):
    if y==0:
        return 1
    return x*exp(x, y-1)
#referenced from stackoverflow

print(exp(2,3))