def bubblesort(arr):
    n=len(arr)
    for i in range(0,n):
         for j in range(0,n-1):
             if(arr[j]>arr[j+1]):
                 (arr[j],arr[j+1])=(arr[j+1],arr[j])
arr=[1,75,27,4,8,3,101,4,2,89]
bubblesort(arr)
print(arr)