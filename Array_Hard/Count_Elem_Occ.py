def count_occ(arr):
    max = float('-inf')
    max_elem = 0
    for elem in arr:
        count_elem = arr.count(elem)
        if count_elem > len(arr)/2:
            max = count_elem
            max_elem = elem
    return max_elem

arr = [4,4,2,4,3,4,4,3,2,4]
print(count_occ(arr))

