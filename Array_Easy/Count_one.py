def count_one(arr):
    for elem in arr:
        count = arr.count(elem)
        if count == 1:
            return elem
arr = [2,1,2,1,2] 
print(count_one(arr))