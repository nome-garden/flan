#8 digital root

ex=12345

def digrt(x): #my attempt... :(
    count=0
    i=0
    for i in range(0, x):
        count+=i
    return(count)

print(digrt(12345))

def digital_root(n):
    return n if n < 10 else digital_root(sum([int(num) for num in str(n)])) #from hevalhazalkurt on Github
