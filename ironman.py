n = 5
a = [[2,4,5],[1,3,6],[2,4,7]]
b = [0,0,0,0,0]
temp= 0
variable = 0
ve = [] 
for j in range(len(a[0])):
        c = a[j]
        if c[0]<c[1]:
            j=c[0]
            while j<c[1]:
                temp = c[2]
                b[j]=b[j]+temp
                j+=1
variable = max(b)            
for i in range(len(b)):
    if variable==b[i]:
        ve.append(i)
        ve.append(i+1)
ve.append(variable)
print(ve)
