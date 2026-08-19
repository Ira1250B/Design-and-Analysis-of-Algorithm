# Linear Search(to get a specific element from an list)
def linear_serach(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i
    return -1
arr=[3,5,78,90,6,8,21,1,4,3]
key=99
result=linear_serach(arr,key)
if(result==-1):
    print("Element not found")
else:
    print("Element found at  ",result)