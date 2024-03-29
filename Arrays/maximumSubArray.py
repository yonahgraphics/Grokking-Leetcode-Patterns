"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
# Time complexity: O(n2)
# Space complexity: O(1)
def maxSubArray1(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        curr_sum = nums[i]
        max_sum = max(curr_sum, max_sum)
        for j in range(i+1, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


# Time complexity: O(n)
# Space complexity: O(1)
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    print(maxSubArray([1,-2,3,1,-2,3,1,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3]))
    print(maxSubArray1([1,-2,3,1,-2,3,1,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3,1,-2,3]))
    print(maxSubArray([-2, 1]))
    print(maxSubArray1([-2, 1]))

























