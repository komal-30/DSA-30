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
print(rotate_mat(mat))