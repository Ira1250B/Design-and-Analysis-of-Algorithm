def minmax(arr):
    if(len(arr)==1):
        return (arr[0],arr[0])
    mid=len(arr)//2
    min1,max1=minmax(arr[:mid])
    min2,max2=minmax(arr[mid:])
    
    if(min1<min2):
        f_min=min1
    else:
        f_min=min2
    if(max1>max2):
        f_max=max1
    else:
        f_max=max2
    return f_min,f_max
arr=[2,4,5,7,1,9,0,3]
print(minmax(arr))
