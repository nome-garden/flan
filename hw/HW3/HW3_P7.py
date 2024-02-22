#7 vowels

vonnegut="Everything was beautiful, and nothing hurt" #vowel count should be 13
hal9000="My mind is going. I can feel it." #vowel count should be 9

count=0
def vwct(x): #referenced from favtutor
    count=0
    i=0
    for i in range(len(x)):
        if(
            x[i]=="a"
            or (x[i]=="A")
            or (x[i]=="e")
            or (x[i]=="E")
            or (x[i]=="i")
            or (x[i]=="I")
            or (x[i]=="o")
            or (x[i]=="O")
            or (x[i]=="u")
            or (x[i]=="U")
        ):
            count += 1
    return(count)

print(vwct(vonnegut))
print(vwct(hal9000))