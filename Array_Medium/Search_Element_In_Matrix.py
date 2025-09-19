
#TC : O(N X M) , Sc: O(1)
def search_elem_matrix(n,m,target,mat):
    for i in range(n):
        for j in range(m):
            if mat[i][j] == target:
                return i,j
    return None


def search_elem_matrix_1(n,m,target,mat):
    for i in range(n):
        if max(mat[i])  >= target:
            for j in range(i,m):
                if mat[i][j] == target:
                    return i,j       
    return None
mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

n = 3
m = 4
target = 8
print(search_elem_matrix_1(n,m,target,mat))



#Time Complexity: O(N + logM)
#O(1)
def binarySearch(nums, target):
    n = len(nums) # size of the array
    low, high = 0, n - 1

    # Perform the steps:
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return binarySearch(matrix[i], target)
    return False