#3 check leap year

def leapyear(x):
    if x%4==0 and x%100!=0: #true if divisible by 4
        return(True)
    elif x%4==0 and x%100==0 and x%400==0: 
        return(True)
    else:
        return(False)
    
print(leapyear(2024))
print(leapyear(2000))
print(leapyear(2003))