'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''
def twoSumIINaive(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i+1, j+1]


# Since we know that the array is sorted, 
# Use two pointers i and j at the end and 
# at the beginning of the array
# increment the i if the sum nums[i] + nums[j] is less than target
# increment decrement j if the sum nums[i] + nums[j] is greater than the target
def towSUmIITwoPointers(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        sum = nums[i] + nums[j]
        if sum == target:
            return [i+1,j+1]
        if sum > target:
            j -= 1
        if sum < target:
            i += 1

if __name__ == "__main__":
    print(twoSumIINaive([1,3,5,6], 7))
    print(towSUmIITwoPointers([1,3,5,6], 7))
            
