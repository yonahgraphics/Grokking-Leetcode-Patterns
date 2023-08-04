# 334. Increasing Triplet Subsequence
# Medium
# Link to problem: https://leetcode.com/problems/increasing-triplet-subsequence/description/
# Given an integer array nums, return true if there exists a triple of
# indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists,
#  return false.

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


# Naive approach
# Time Complexity: O(n3)
# Space Complexity: O(1)
def increasingTriplet(nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            if len(nums) < 3:
                return False

            for i in range(len(nums)-2):
                for j in range(i + 1, len(nums)-1):
                    for k in range(j + 1, len(nums)):
                        print(nums[i], nums[j], nums[k])
                        if (nums[i] < nums[j]) and (nums[j] < nums[k]):
                            return True
            return False



# Optimum approach
# Time Complexity: O(1)
# Space Complexity: O(1)
def increasingTriplet(nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            if len(nums) < 3:
                return False

            first_min = float('inf')
            second_min = float('inf')

            for num in nums:
                if num <= first_min:
                    first_min = num
                elif num <= second_min:
                    second_min = num
                else:
                    print(first_min, second_min, num)
                    return True
            return False

if __name__ == "__main__":
    print(increasingTriplet([2,1,5,0,4,6]))
