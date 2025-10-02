
#Brute Force
#TC = O(nxm) + O(nxm)
#SC = O(1)
def set_mat_zero(mat):
    zero_row = set()
    zero_col = set()
    n=len(mat)
    m = len(mat[0])
    #First Find the indices which have zero
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for i in range(n):
        for j in range(m):
            if i in zero_row:
                mat[i][j] =0
            if j in zero_col:
                mat[i][j] =0
    print(zero_col)
    print(zero_row)
    return mat

mat=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_mat_zero(mat))


#Optimal Approch
    




