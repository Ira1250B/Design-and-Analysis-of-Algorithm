def partition(arr,start,end):
    pindex=start
    pivot=arr[end]

    for i in range(start,end):
        if(arr[i]<=pivot):
            (arr[i],arr[pindex])=(arr[pindex],arr[i])
            pindex=pindex+1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    return pindex  

def quicksort(arr,start,end):
    if(start<end):
        pi=partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)
    return arr


arr=[4,51,3,7,8,9,1,0]
print(quicksort(arr,0,len(arr)-1))

