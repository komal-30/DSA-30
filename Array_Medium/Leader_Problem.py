def leader_problem(arr):
    leader_list = []
    leader_list.append(arr[-1]) 
    for i in range(len(arr)-2,-1,-1):
        if arr[i] < arr [i-1]:
            leader_list.append(arr[i-1])
    return leader_list
arr = [10, 22, 12, 3, 0, 6]
print(leader_problem(arr))

   