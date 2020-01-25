'''
Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.
'''


# solution not complete. Please dont copy

count = 0

#dynamic programming method, this takes O(sum*n) time
def does_total_exist(total, arr):
    n = len(arr)
    dp_mat = [[False for i in range(total+1)] for j in range(n+1)]

    for i in range(n+1):
        dp_mat[i][0] = True  

    for i in range(1, total+1):
        for j in range(1, n+1):
            one = dp_mat[j-1][i- arr[:j][-1]] if ((i-arr[:j][-1]) >= 0) else False
            two = dp_mat[j-1][i]

            dp_mat[j][i] = one or two 

    return dp_mat



def recur_path(dp_mat, arr, n, total, pizza_types):

    # p = pizza_types.copy()
    if total == 0:
        print(pizza_types)
        return 

    elif total < 0:
        return
    
    # elif n > 0 and dp_mat[n][total] == True:
    if n > 0:
        if dp_mat[n-1][total] == True:
            b = pizza_types.copy()
            recur_path(dp_mat, arr, n-1, total, b)

        if total - arr[n-1] >= 0 and dp_mat[n-1][total-arr[n-1]] == True:
            # if arr[:n][-1] == 5:
            # print(f'pizza_types : {pizza_types}')
            pizza_types.append(arr[n-1])
            recur_path(dp_mat, arr, n-1, total-arr[n-1], pizza_types)

    return 


total= 100
arr = [4, 14, 15, 18, 29, 32, 36, 82, 95, 95]
# arr = [1,1,2,3,5]
n = len(arr)
dp_mat = does_total_exist(total, arr)
# print(dp_mat)
print(recur_path(dp_mat, arr, n, total, []))