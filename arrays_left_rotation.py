# Hackerrank problem url
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

arr = [1, 2, 3, 4, 5]

# arr is the arry & d is the number of rotations


def rotLeft(arr, d):
    n = len(arr)
    # if number of rotations is equal to the length
    # of the array then return the array itself
    if n == d:
        return arr
    else:
        arr_1 = arr[:d]
        arr_2 = arr[d:]
        return arr_2 + arr_1


print(rotLeft(arr, 4))
