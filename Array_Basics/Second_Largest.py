'''
Edge Cases
    ----------
    - arr = [5] -> None (only one element, no second smallest/largest)
    - arr = [1, 2] -> None (only two elements, no second smallest/largest)
    - arr = [3, 3, 3] -> None (all elements same, no valid second smallest/largest)
    - arr = [1, 2, 2, 7, 7] -> (2, 2) (handles duplicates correctly)
    - arr = [-10, -5, -1, 0] -> (-5, -1) (works with negatives)

Time Complexity: O(n)
Space Complexity: O(1)

'''



def second_large_small(arr):
    largest = max(arr) # 7 
    smallest = min(arr) # 1
    second_largest = float('-inf')
    second_smallest = float('inf')
    
    for num in arr:
        if num != largest and num !=smallest:
            if num>second_largest:
                second_largest= num
            if num<second_smallest:
                second_smallest= num
    print("Second smallest is", second_smallest)
    print("Second largest is", second_largest)

arr = [1, 2, 4, 6, 7, 5]
print(second_large_small(arr))