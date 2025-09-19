def missing_elem(arr, N):
    total = N * (N + 1) // 2
    return total - sum(arr)

arr = [1, 2, 4, 5]
print(missing_elem(arr, 5))  


def missing_elem(arr, N):
    xor_all = 0
    xor_arr = 0
    
    for i in range(1, N+1):
        xor_all ^= i
    for num in arr:
        xor_arr ^= num
    
    return xor_all ^ xor_arr