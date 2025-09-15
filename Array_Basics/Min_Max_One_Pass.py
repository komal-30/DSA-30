def min_max_one_pass(arr):
    if not arr:
        return None
    else:
        min = arr[0]
        max = arr[0]
        for num in arr:
            if num > max:
                max = num
            if num < min:
                min = num
        return max,min
    
arr = [-2,-3,-2]
print(arr.index(-2))
print(min_max_one_pass(arr))
