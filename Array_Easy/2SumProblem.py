def two_sum(arr,target):
    for ind1 in range(len(arr)):
        for ind2 in range(ind1+1,len(arr)):
            if arr[ind1] +arr[ind2] == target:
                return ind1,ind2
            
    return[-1,-1]

arr = [2,6,5,8,11]
target = 15
print(two_sum(arr,target))
