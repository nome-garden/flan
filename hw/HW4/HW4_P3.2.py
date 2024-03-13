"3.2"
biglist = []
for i in range(0,5):
    n = []
    for j in range(1,6):
        n.append(j+5*i)
    biglist.append(n)
print("3.1: ",biglist)

anotherlist=[]
for q in biglist:
    n=[]
    for r in q:
        if r%3==0:
            n.append("?")
        else:
            n.append(r)
    anotherlist.append(n)
print("3.2: ", anotherlist)

#thanks owen for suggestions and advice!!! :D