def shift_left(arr,k):
    for ind in range(k):
        elem = arr[ind]
        arr.pop(ind)
        arr.append(elem)
    return arr

print(shift_left([3, 1, 4],2))


