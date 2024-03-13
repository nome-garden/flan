"2.3"
lsA=list(range(1,11))
lsB=list(range(20,31))
lsC=[]

def odd(m):
    if m%2!=0:
        lsC.append(m)

for i in lsA:
    m=i
    odd(m)

for i in lsB:
    m=i
    odd(m)

print("lsA: ",lsA) #to check
print("lsB: ",lsB) #to check
print("(2.3) lsC: ", lsC)

#first when running, list showed as [1, None, 3, None, ...]
#second try, list showed as [1, (), 3, (), ...]
#fourth try I removed lsc.append(odd(m)) for each of the for i's, and added it instead to the if-statement and it works!!! :D