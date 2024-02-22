#5 rotating digits

def rotate_digits(n): 
    pt1=str(n%10)
    pt2=str(n//10)
    pt3=pt1+pt2
    result=int(pt3)
    return(result)
#referenced from stackoverflow
print(rotate_digits(12345))
print(rotate_digits(8886))