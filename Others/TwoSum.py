''''
Given an array of numbers and a target sum, find a pair in the array whose
sum is equal to the given target.
Leetcode: https://leetcode.com/problems/two-sum/

'''
# Use a nested loop to get all possible combinations of the sum of two
# Compare with the target
# Return the indexes if they equal the target
def twoSumNaive(arr, target): # O(n2) time, O(1) space
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return -1


# Use a hashmap to keep all visited nums
# Check if the diff btn the target and nus starting with the second one are
# in the hasmap, if so, return the idx of the current num and the idx in
# the map that corresponds to the diff
def twoSumOptimum(arr, target): # O(n) time, O(n) space
    visited = {} # num : idx

    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in visited:
            return [visited[diff], i]

        visited[arr[i]] = i


if __name__ == "__main__":
    print(twoSumOptimum([1,3,4,5], 7))
    print(twoSumNaive([1,3,4,5], 7))
