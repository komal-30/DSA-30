def dup_elem(arr):
    arr_dup =[]
    for elem in arr:
        if elem not in arr_dup:
            arr_dup.append(elem)
        else:
            return elem

arr = [3,1,3,4,2]
print(dup_elem(arr))