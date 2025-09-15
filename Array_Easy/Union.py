def union(arr1,arr2):
    return sorted(list(set(arr1+arr2)))

arr1=[1,2,3,4,5]
arr2=[2,3,4,4,5]
print(union(arr1,arr2))