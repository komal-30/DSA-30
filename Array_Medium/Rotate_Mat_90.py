#Brute- Force This solution always works
#TC = o(n2) SC=O(nxm)
def rotate_mat(mat):
    m = len(mat)
    n = len(mat[0])
    new_mat = [[0] * m for _ in range(n)]    
    for i in range(m):
        for j in range(n):
            new_mat[i][j] = mat[x][y]
        y=-1
    return new_mat
mat =  [[1,2,3],[4,5,6],[7,8,9]]
#print(rotate_mat(mat))

#Optimal Solution-Only works for square matrix - n=m
#TC : O(N*N) + O(N*N),SC = O(1)
def rotate(matrix):
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            #Swaping without temp variable - tuple unpacking swap trick.
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

def stock_buy_sell(arr):
    maxi= float('-inf')
    mini = min(arr)
    index_mini = arr.index(mini)
    for elem in arr[index_mini:]:
	    if elem>mini and elem>maxi:
		    max= elem
    return maxi-mini
arr = [7,1,5,3,6,4]
print(stock_buy_sell(arr))