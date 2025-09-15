def remove_dups(arr):
    dup=[]
    for elem in arr:
        if  elem not in dup:
            dup.append(elem)
    dup += (len(arr) - len(dup)) * [0]
    return  dup
arr = [1,1,1,2,2,3,3,3,3,4,4]
print(remove_dups(arr))
