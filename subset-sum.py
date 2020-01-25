#recursive method, this takes like exponential time
def ss(total, arr):
    arr1 = arr.copy()
    arr2 = arr.copy()
    if arr:
        curr = arr1.pop()
        arr2.pop()
        if total-curr == 0:
            return 1

        one = ss((total-curr), arr1) if (total>=curr) else 0  
        two = ss(total, arr2)

        return one or two 
    return 0 


#dynamic programming method, this takes O(sum*n) time
def dp_ss(total, arr):
    n = len(arr)
    dp_mat = [[0 for i in range(total+1)] for j in range(n+1)]

    for i in range(n+1):
        dp_mat[i][0] = 1 

    for i in range(1, total+1):
        for j in range(1, n+1):
            one = dp_mat[j-1][i- arr[:j][-1]] if ((i-arr[:j][-1]) >= 0) else 0 
            two = dp_mat[j-1][i]

            dp_mat[j][i] = one or two 

    return dp_mat[n][total]

print(dp_ss(56, [1,3,2,5,7,10,11,3,78,1,2,2,2,2,10]))
print(ss(56, [1,3,2,5,7,10,11,3,78,1,2,2,2,2,10]))

            