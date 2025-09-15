def search(arr,n):
    for ind in range(0,len(arr)):
        if n == arr[ind]:
            return ind 
    return -1
arr = [1,2,3,4,7]
n = 7
print(search(arr,n))