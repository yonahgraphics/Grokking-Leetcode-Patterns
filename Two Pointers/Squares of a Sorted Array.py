'''
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

# Square and sort
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    nums.sort() # O(nlogn) time and O(n) space due to timsort
    return nums

# Two Pointer Approach
# Since we can have negative numbers, we may not have a sorted squares result.
# We can put one pointer at the beginning and the other at the end and keep comparing
# the values at those postns, keeping the greater one and shifting the pointers accordingly until the
# pointers cross.
# Then we can sort the result in ascending order and return it
# Time Complexity: O(n)
# Space Complexity: O(n)
def sortedSquares1(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    res = []
    
    while left <= right:
        if nums[left]*nums[left] > nums[right]*nums[right]:
            res.append(nums[left]*nums[left])
            left += 1
        else:
            res.append(nums[right]*nums[right])
            right -= 1
    
    return res[::-1]
            
if __name__ == "__main__":
    print(sortedSquares([-2, 1, 3]))
    print(sortedSquares([-2, 1, 3]))
        