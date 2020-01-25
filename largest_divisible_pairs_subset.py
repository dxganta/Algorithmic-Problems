'''

Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the 
larger element of the pair is divisible by smaller element.

'''

def ldps(n, arr):
    arr = sorted(arr)
    scores = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i)[::-1]:
            if arr[i] % arr[j] == 0:
                scores[i] += scores[j]
                break
    return max(scores)


arr = [18,1,3,6,13,17]
n = len(arr) 
print(ldps(n, arr))

