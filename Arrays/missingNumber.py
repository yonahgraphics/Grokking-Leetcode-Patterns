'''
Missing Number
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all 
numbers are in the range [0,3]. 2 is the missing number 
in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers
are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

'''

#Approach1: Sorting
#Time complexity: O(nlogn)
#Space complexity: O(n) due to timsort space requirement
def missingNumber1(nums):
    nums.sort()
    if nums[-1] < len(nums):
        return nums[-1] + 1
    if nums[0] != 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            return  nums[i-1] + 1

# Approach2: Hashset
# Time complexity: O(2N) === O(N) due to the two for loops
# Space complexity: O(N) due to the hashset
def missingNumber2(nums):
    seen = set()
    for num in nums:
        seen.add(num)
    for i in range(len(nums)+1):
        if i not in seen:
            return i

# Approach3: Simple logic
# Time complexity: O(2N) === O(N) due to the two for loops
# Space complexity: O(1)
def missingNumber3(nums):
    givenSum = 0
    totalSum = 0
    for num in nums:
        givenSum += num
    for i in range(len(nums)+1):
        totalSum += i
    return totalSum - givenSum

# Time complexity: O(n)
# Space complexity: O(1)
def missingNumber4(nums):
   res = 0
   for i in range(len(nums)+1):
       res ^= i
   for num in nums:
       res ^= num
   return res

if __name__ == "__main__":
    print(missingNumber1([0,1]))
    print(missingNumber2([0,1]))
    print(missingNumber3([0,1]))
    print(missingNumber4([0,1]))