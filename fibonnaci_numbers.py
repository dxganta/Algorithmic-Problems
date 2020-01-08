
''' Getting the nth number from the Fibonnaci Series'''

# using simple recursive method
def fib(n):
    if n <= 1:
        return n

    else:
        return fib(n-2) + fib(n-1)



# using the memoization technique of Dynamic Programming
def fib_memoiz(n):
    fib_arr = [None] * (n+1)
    fib_arr[0] = 0
    if n > 0:
        fib_arr[1] = 1

    if n > 1:
        if fib_arr[n] != None:
            return fib_arr[n]
        else:
            fib_arr[n] = fib_memoiz(n-1) + fib_memoiz(n-2)

    return fib_arr[n] 


# using the tabulation method of Dynamic Programming
def fib_tabular(n):
    fib_arr = [None] * (n+1)
    fib_arr[0] = 0

    if n > 0:
        fib_arr[1] = 1
    
    if n > 1:
        for i in range(2, n+1):
            fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]

    return fib_arr[-1]

print(fib_tabular(9))