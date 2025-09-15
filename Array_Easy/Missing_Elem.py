def missing_elem(arr):
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] !=1:
            return arr[i] + 1
arr = [1,3]
print(missing_elem(arr))