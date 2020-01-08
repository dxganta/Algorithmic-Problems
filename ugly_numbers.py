def ugly_numbers(n):

    arr = [0] * n
    arr[0] = 1

    i = 0
    j = 0
    k = 0

    mul_2 = arr[i] * 2
    mul_3 = arr[i] * 3
    mul_5 = arr[i] * 5

    for s in range(1, n):
        ugly_num = min(mul_2, mul_3, mul_5)
        arr[s] = ugly_num
        if ugly_num == mul_2:
            i += 1
            mul_2 = arr[i] * 2 
        if ugly_num == mul_3:
            j += 1
            mul_3 = arr[j] * 3

        if ugly_num == mul_5:
            k += 1
            mul_5 = arr[k] * 5
    return arr[-1]


print(ugly_numbers(150))