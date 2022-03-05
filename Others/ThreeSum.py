def threeSum(nums): # O(n3)
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                # Ensure the condition is met and
                    if nums[i] + nums[j] + nums[k] == 0:
                        soln = [nums[i], nums[j], nums[k]]
                        # Sort to ensure we are not adding dublicates
                        soln.sort()
                        if soln not in res:
                            res.append(soln)
        return res
    
    
def threeSumOptimum(nums): # O(n2)
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

if __name__ == "__main__":
    print(threeSum([-4,1,1,2,2,3,3]))
    print(threeSumOptimum([-4,1,1,2,2,3,3]))
            
        
        