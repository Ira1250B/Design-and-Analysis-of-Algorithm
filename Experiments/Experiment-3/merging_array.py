def merging_array(a,b):
    i,j,k=0,0,0
    c=[0]*(len(a)+len(b))
    while(i<len(a)and j<len(b)):
        if(a[i]<b[j]):
            c[k]=a[i]
            i+=1
            k+=1
        else:
            c[k]=b[j]
            j+=1
            k+=1
    while(i<len(a)):
        c[k]=a[i]
        i+=1
        k+=1
    while(j<len(b)):
        c[k]=b[j]
        j+=1
        k+=1
    return c
a=[1,3,5,9,11]
b=[2,4,8,16,24,30]
print(merging_array(a,b))