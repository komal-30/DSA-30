def smallest_element(arr):
    if not arr:
        return None
    min = arr[0]
    for elem in arr:
        if elem<min:
            min = elem
    return min
arr = [2,3,1,-1,0,4]
print(smallest_element(arr))
