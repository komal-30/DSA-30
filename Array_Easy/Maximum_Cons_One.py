'''
Edge Cases:
        - [] -> 0 (empty array)
        - [0,0,0] -> 0 (all zeros)
        - [1,1,1] -> len(arr) (all ones)
        - [1,0,1,1,0,1] -> 2 (streak in middle)
        - [0,1,1,1,0,1] -> 3 (streak in middle)
        - [1] -> 1 (single element one)
        - [0] -> 0 (single element zero)
        - [1,0,1,0,1,0] -> 1 (alternating)

Time Complexity: O(n) where n = length of arr
Space Complexity: O(1), uses only constant extra space
'''


def max_one(arr):
    count = 0
    max_count = 0
    for elem in arr:
        if elem == 0:
            max_count=count
            count = 0
        else:
            count+=1
    return max(count,max_count)
arr = [1, 1, 1, 1, 0, 1]
print(max_one(arr))