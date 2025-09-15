'''
Edge Cases:
        - [] -> []
        - [0, 0, 0] -> [0, 0, 0] (all zeros remain at end)
        - [1, 2, 3] -> [1, 2, 3] (no zeros, unchanged)
        - [1, 0, 2, 0, 3] -> [1, 2, 3, 0, 0]
        - [0] -> [0]
        - [5] -> [5]

    Time Complexity: 
        O(n) — one pass to count zeros, one pass to build non-zero list,
        and one operation to append zeros. (Two passes but still linear.)

    Space Complexity:
        O(n) — because a new list is created to hold non-zero elements.
'''

def move_zero_to_end(arr):
    count_zero = arr.count(0)
    arr = [elem for elem in arr if elem != 0 ]
    arr += [0] * count_zero
    return arr

arr = [1,2,0,1,0,4,0]
print(move_zero_to_end(arr))


'''
Two Pointer Approach
Time Complexity: O(n)
Space Complexity: O(1)
'''
def move_zero_to_end_inplace(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr




