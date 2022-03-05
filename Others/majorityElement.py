''''
Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Leetcode link: https://leetcode.com/problems/majority-element/
'''

# Naive approach1: 
# Time Complexity:  O(n2)
# Space Comlexity: O(1)
def majorityElement1(nums):
    count = 0
    majority = len(nums)//2
    element = -1
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count > majority:
            return nums[i]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def majorityElement2(nums):
    freq = {}
    max_count = 0
    result = 0
    for num in nums: #O(n)
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 
        if freq[num] > max_count:
            result = num
            max_count = freq[num] 
    return result

# Sorting the array
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def majorityElement3(nums): 
        nums.sort()
        target_idx = len(nums)//2
        return nums[target_idx]

# Boyer-Moore Voting Algorithm

# Choosing and maintaining the majority element as long as it's count 
# does not become 0. Once it becomes 0, you drop it and pick the next 
# as the next element. At the end, the majority element variable will
# contain the majority element
# Time Complexity: O(n)
# Space Complexity: O(1)

def majorityElement4(nums):
        maj_element = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if maj_element == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_element = nums[i]
                count = 1
        return maj_element

if __name__ == "__main__":
    print(majorityElement1([1,2,2,2,9]))
    print(majorityElement2([1,2,2,2,9]))
    print(majorityElement3([1,2,2,2,9]))
    print(majorityElement4([1,2,2,2,9]))
