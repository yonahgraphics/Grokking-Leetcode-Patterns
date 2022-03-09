# Time Complexity: O(n^2)
# Space Complexity: O(1)
def threeSumClosest(nums, target):
    nums.sort()
    closestSum = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]: # Removes duplicate solutions
            continue 
        l = i+1
        r = len(nums)-1
        while l < r:
            theSum = nums[i] + nums[l] + nums[r] 
            if theSum > target:
                r -= 1
                
            elif theSum < target:
                l += 1
            else: 
                return theSum
            
            if abs(theSum - target) < abs(closestSum - target):
                closestSum = theSum
    return closestSum
    

if __name__ == "__main__":
#  [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    print(threeSumClosest([-1,2,1,-4], 1))

      