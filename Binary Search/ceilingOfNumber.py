'''
Given a sorted array of distinct integers and a target value, return 
the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

 Leetcode link: https://leetcode.com/problems/search-insert-position/

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
'''
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums)-1
    found = False
    
    while low <= high:
        mid = low  + (high - low)//2
        
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid +1
        else:
            return mid
    return low

if __name__ == "__main__":
    print(searchInsert([1,2,3,4,7,8], 9))
            
        