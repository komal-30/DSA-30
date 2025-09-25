def longest_cons(arr):
    max_count = float('-inf')
    count = 0
    for ind in range(len(arr)-1):
        if arr[ind] < arr[ind+1]:
            count+=1
        else:
            max_count = count
            count=0

    return max_count
arr =  [100, 200, 1, 3, 2, 4]
print(longest_cons(arr))

