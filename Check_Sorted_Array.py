''' 
Important Test Cases:  
1. Empty array → [] → should return True (edge case).  
2. Single element → [5] → should return True.  
3. Two elements sorted → [2, 5], [3, 3] → should return True.  
4. Two elements unsorted → [5, 2] → should return False.  
5. Already sorted → [1, 2, 3, 4] → should return True.  
6. Strictly decreasing → [9, 7, 5, 3] → should return False.  
7. Array with negatives → [-3, -2, -2, 0] → should return True.  
8. Large input (10^6 elements) → performance check. 
'''

'''
Optimized Approach I
Time Complexity (TC): O(n) → The array is traversed once to check order.  
Space Complexity (SC): O(1) → Only constant extra space is used. 
'''

def is_sorted(arr):
    if not arr:
        return False
    prev = arr[0]
    for elem in arr:
        if elem-prev < 0:
            return False
        prev = elem
    return True

arr = [5,4,6,7,8]
#print(sorted(arr))


'''
Optimized Approach II
Time Complexity (TC): O(n) → The array is traversed once to check order.  
Space Complexity (SC): O(1) → Only constant extra space is used. 
'''

def is_sorted(arr):
    if not arr:
        return False
    for ind in range(0,len(arr) - 1):
        if arr[ind] > arr[ind+1]:
            return False
    return True

arr = [1]
print(is_sorted(arr))


'''
Brute Force Approach 
Time Complexity (TC): O(n) → The array is traversed once to check order.  
Space Complexity (SC): O(1) → Only constant extra space is used. 
'''

def is_sorted(arr):
    if not arr:
        return False
    for i in range(len(arr)):
        for j in (i+1,len(arr)):
            if arr[j] < arr[i]:
                return False

    return True

arr = [1]
print(is_sorted(arr))