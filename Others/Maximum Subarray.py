'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
Leetcode link: https://leetcode.com/problems/maximum-subarray/
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1

Algorithm:
----------
Set the max sum to a very large negative number, curr_sum to 0 and start iterating
over the array adding each number to the curr_sum. Every time the curr_sum becomes negative,
reset it to 0. Compare the max sum with the curr max sum and update it if you got a bigger max sum
then finally return the max sum

YouTube video link: https://www.youtube.com/watch?v=5WZl3MMT0Eg

'''

# Time complexity: O(n)
# Space Complexity: O(1)
def maxSubArray(nums):
    max_sum = float('-inf')
    curr_sum = 0
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum
        
if __name__ == "__main__":

    #Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    #Output: 6
    #Explanation: [4,-1,2,1] has the largest sum = 6.

    array = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(array))