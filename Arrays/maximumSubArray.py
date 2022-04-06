
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)                
    return max_sum

if __name__ == "__main__":
    print(maxSubArray([1,-2,3]))


        
    
        
        
        
        
        
        
        
       
    
    
    
    
    
    
    
    
    
    
    
    
    