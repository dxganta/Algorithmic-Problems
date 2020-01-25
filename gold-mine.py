
def dp_gold(rows, columns, mat):

    if rows == 1:
        return sum(mat[0])

    if columns == 1:
        high_gold = 0
        for i in range(rows):
            high_gold = max(high_gold, mat[i][0])

        return high_gold 

    for col in range(columns-1)[::-1]:
        for row in range(rows): 
            if row == 0:
                mat[row][col] += max(mat[row][col+1], mat[row+1][col+1])
            elif row == (rows-1):
                mat[row][col] += max(mat[row][col+1], mat[row-1][col+1])
            else:
                mat[row][col] += max(mat[row-1][col+1], mat[row][col+1], mat[row+1][col+1])

    max_gold = 0
    for i in range(rows):
        max_gold = max(max_gold, mat[i][0])

    return max_gold 


mat1 = [[10], 
        [33], 
        [13], 
        [15]]

mat2 = [[10,33,13,15]]

mat3 = [[36, 5,  46, 29, 13, 57, 24, 95], 
        [82, 45, 14, 67, 34, 64, 43, 50],
        [87, 8,  76, 78, 88, 84, 3,  51], 
        [54, 99, 32, 60, 76, 68, 39, 12],
        [26, 86, 94, 39, 95, 70, 34, 78]]


print(dp_gold(5,8, mat3))














[[1, 3, 1, 5],
 [2, 2, 4, 1],
 [5, 0, 2, 3],
 [0, 6, 1, 2]]









