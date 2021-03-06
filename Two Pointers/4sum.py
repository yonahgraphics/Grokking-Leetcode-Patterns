# Time Complexity: O(n^3)
# Space Complexity: O(n) # Due to the result array

def fourSum(nums, target):
    nums.sort()
    result = []

    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j + 1
            r = len(nums)-1
            
            while l < r:
                if nums[i] + nums[j] + nums[l] + nums[r] > target:
                    r -= 1
                elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    result.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r: # We keep shifting the left pointer to avoid duplicates w
                        l += 1
    return result


# You could also just use a set to avoid duplicates
def fourSum1(nums, target):
    ans = set()
    n = len(nums)
    nums.sort()
    for i in range(n):
        for j in range(i+1,n):
            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]+nums[j]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    ans.add((nums[i], nums[left], nums[right],nums[j]))

                    left += 1
                    right -= 1
    return ans

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
if __name__ == "__main__":
    print(fourSum([1,0,-1,0,-2,2], 0))
    print(fourSum1([1,0,-1,0,-2,2], 0))