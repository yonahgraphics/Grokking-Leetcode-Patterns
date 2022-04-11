"""
https://leetcode.com/problems/rotate-array/

189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
# Time Complexity: O(n)
# Space Complexity: O(n)
def rotate(nums, k):
    k = k % len(nums)     #take care of the case where k >= len(nums)  
    nums[:] = nums[-k:] + nums[:-k] 
    return nums

# Time Complexity: O(n)
# Space Complexity: O(n)
def rotate1(nums, k):
    res = [0]*len(nums)
    for i in range(len(nums)):
        shiftIndex = (i + k)%len(nums)
        # print("shifted: ", shiftIndex, "val", nums[i])
        res[shiftIndex] = nums[i]
    nums = res
    return nums

print(rotate1([1,2,3,4], 2))
print(rotate([1,2,3,4], 2))