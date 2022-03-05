# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’
# https://leetcode.com/problems/largest-subarray-length-k/

import math
def maximumSumNaive(array, k): # O(n*k)
    i = 0
    j = k

    while j <= len(array):
        subArray = array[i:j]
        sum = 0
        maximum = -math.inf
        for num in subArray:
            sum += num
        maximum = max(maximum, sum)
        i += 1
        j += 1
    return maximum


def maximumOptimum(array, k): # O(n)
    i = 0
    j = k
    subArray = array[i:k] 
    sum = 0
    maximum = -math.inf
    for num in subArray:
        sum += num
    while j < len(array):
        sum = sum + array[j] - array[i]
        maximum = max(sum, maximum)
        i += 1
        j += 1
    return maximum

if __name__ == "__main__":
    print(maximumSumNaive([1,2,3,4,5], 2))
    print(maximumOptimum([1,2,3,4,5], 2))

