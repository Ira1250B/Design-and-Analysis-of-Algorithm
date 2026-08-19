def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merging_array(left,right)

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
arr=[2,1234,56,2,34,7,8,9,100]
    


