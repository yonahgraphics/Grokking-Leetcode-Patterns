
"""
1985. Find the Kth Largest Integer in the Array

You are given an array of strings nums and an integer k. Each string in nums represents 
an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], 
"2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
Example 1:

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
Example 2:

Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".
"""

# Approach 1: Sorting
# Time complexity: O(nlogn)
# Space complexity: O(1)
def kthLargestNumber(self, nums, k):
    for i, num in enumerate(nums):
        nums[i] = int(num)
    nums.sort(reverse = True)
    return str(nums[k-1])