# recursive method for calculating binomial coefficients
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    elif k == 1:
        return n 

    return binomial(n-1, k-1) + binomial(n-1,k)

# using tabulation method from dynamic programming
def binomial_tab(n,k):
    b_arr = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i+1, k+1)):
            if j == 0  or j == i:
                b_arr[i][j] = 1
            elif j == 1:
                b_arr[i][j] = i 

            else:
                b_arr[i][j] = b_arr[i-1][j-1] + b_arr[i-1][j]

    return b_arr[n][k]

print(binomial_tab(5,2))
print(binomial(5,2))