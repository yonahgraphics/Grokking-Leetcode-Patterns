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

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    if __name__ == "__main__":
        print(fourSum([1,0,-1,0,-2,2], 0))