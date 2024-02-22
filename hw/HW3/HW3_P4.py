#4 calculating BMI

def BMI(x,y): #in kgs (x) and meters (y)
    result = x/(y**2)
    return(result)

print(BMI(63.5,1.55))