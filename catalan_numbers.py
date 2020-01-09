
# recursive method for getting nth catalan number
def catalan(n):
    total = 0
    if n <= 1:
        return 1

    if n > 1:
        for i in range(n):
            total += catalan(i) * catalan(n-1-i)

    return total 


#using tabulation method from Dynamic Programming
def catalan_tab(n):
    cat_arr = [None] * (n+1)
    cat_arr[0] = 1

    if n > 0:
        cat_arr[1] = 1

    if n > 1:
        for i in range(2, n+1):
            total = 0
            for j in range(i):
                total += cat_arr[j] * cat_arr[i-1-j]
            cat_arr[i] = total
    return cat_arr[n]

print(catalan_tab(4))

    