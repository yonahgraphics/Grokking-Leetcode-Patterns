"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the
 integers in the range [1, n] that do not appear in nums.
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

# Time complexity: O(n)
# Space complexity: O(1)
def findDisappearedNumbers(nums):
    seen = set(nums)
    res = []
    for i in range(1, len(nums)+1):
        if i not in seen:
            res.append(i)
    return res

# Time complexity: O(n)
# Space complexity: O(1)
def findDisappearedNumbers1(nums):
    res = []
    for num in nums:
        index = abs(num)-1
        nums[index] = -1*abs(nums[index])
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res




if __name__ == "__main__":
    print(findDisappearedNumbers([1,3,3,3]))
    print(findDisappearedNumbers1([1,3,3,3]))
