# recursive method for getting nth bell number for k partitiions

def bell(n,k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    elif k == n:
        return 1

    else:
        return (k * bell(n-1, k)) + bell(n-1, k-1)

# tabulation method from Dynamic Programming
def bell_tab(n,k):
    bell_arr = [[0 for s in range(k+1)] for t  in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1,k+1)):
            if j == 1 or i == j:
                bell_arr[i][j] = 1
            else:
                bell_arr[i][j] = j * bell_arr[i-1][j] + bell_arr[i-1][j-1]

    return bell_arr[n][k]


print(bell_tab(10,4))
print(bell(10,4))