#4 Everything is in order
import numpy as np

np.random.seed(12345)
a=np.random.randint(1,50,(4,5))
print(a)

def sorting(x):
    return(np.sort(x,axis=0))

print(sorting(a))