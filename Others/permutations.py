"""
Leetcode link: https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the 
possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
"""

def permute(nums):
    result = []
        
    if len(nums) == 1:
        return [nums.copy()]
        
    for i in range(len(nums)):
        n = nums.pop(0)
            
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result


if __name__ == "__main__":
    print(permute([1,2]))