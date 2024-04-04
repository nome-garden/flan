#3 I Need Some Space

import numpy as np

myarr=np.array(['python','is','cool!'])

def spaceBetween(n):
    return(np.char.replace(n,""," ")) 

print(spaceBetween(myarr))
print(type(spaceBetween(myarr)))
print(np.shape(spaceBetween(myarr)))