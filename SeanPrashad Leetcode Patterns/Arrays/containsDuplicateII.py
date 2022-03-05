'''
Given an integer array nums and an integer k, return true if there
 are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

https://leetcode.com/problems/contains-duplicate-ii/
'''
#Aproach1: Bruteforce (Exceed max time on leetcode)
#Time complexity: O(n2)
#Space complexity: O(1)
def containsNearbyDuplicate1(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


#Approach2: Hashmap
#Time complexity: O(n)
#Space complexity: O(n)
def containsNearbyDuplicate2(nums, k):
    visited = {}
        
    for idx, num in enumerate(nums):
        if num in visited and abs(visited[num] - idx) <= k:
            return True
        else:
            visited[num] = idx
    return False

if __name__ == "__main__":
    # Input: nums = [1,2,3,1], k = 3
    # Output: true

    # Input: nums = [1,2,3,1,2,3], k = 2
    # Output: false
    nums, k =  [1,2,3,1], 3
    print(containsNearbyDuplicate1(nums, k))
    print(containsNearbyDuplicate2(nums, k))
