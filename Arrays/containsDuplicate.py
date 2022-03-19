'''
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true

https://leetcode.com/problems/contains-duplicate/
'''

#Approach 1: Sorting
# Time Complexity: O(nlogn), when n is the length of the array
# Space complexity: O(n) because Timsort uses O(n) space in the worst case
def containsDuplicate1(nums):
    if len(nums) <= 0:
        return False
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

#Approach 2: Bruteforce
# Time Complexity: O(n2) because of the two loops
# Space complexity: O(1)
def containsDuplicate2(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

#Approach 3: hasset
# Time Complexity: O(n) because of we scan thru the array
# Space complexity: O(n) b'se of the hashset
def containsDuplicate3(nums):
    seen  = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(containsDuplicate1([1,3,2,5,2]))
    print(containsDuplicate2([1,3,2,5,2]))
    print(containsDuplicate3([1,3,2,5,2]))




