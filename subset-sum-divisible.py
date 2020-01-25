'''
Subset with sum divisible by m

Given a set of non-negative distinct integers, and a value m, determine if there is a subset of the given set with sum divisible by m.
Input Constraints
Size of set i.e., n <= 1000000, m <= 1000'''


def ds(m_var, m_fix, arr):
    arr1 = arr.copy()
    arr2 = arr.copy()
    if arr:
        curr = arr1.pop()
        arr2.pop()
        if (m_var+curr) % m_fix == 0:
            return 1

        one = ds(m_var+curr, m_fix, arr1)
        two = ds(m_var, m_fix, arr2)

        return one or two 
    return 0 
