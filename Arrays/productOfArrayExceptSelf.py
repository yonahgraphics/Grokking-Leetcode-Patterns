"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

#Approach 1:
#Time complexity: O(n^2)
#Space complexity: O(n)

def productExceptSelf(nums):
    res = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j == i:
                continue
            product *= nums[j]
        res.append(product)
    return res

#Approach 2:
#Points to note about this approach
# Works only if the input array does not contain any zeros
# Won't be accepted since we can't use a division operator
# Time complexity: O(n)
# Space complexity: O(n)

def productExceptSelf1(nums):
        res = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        
        for j in range(len(nums)):
            res.append(int(product/nums[j]))
        return res

#Approach 3:
# Precalculate the prefix and postfix products for each element
# Then multiply the corresponding prefix and postfix
# Time complexity: O(n)
# Space complexity: O(n)

def productExceptSelf2(nums):
    prefixArray  = [1]
    postfixArray = [1]
    
    res = []
    
    # Populate prefix array
    for i in range(len(nums)-1):
        prefixArray.append(prefixArray[-1]* nums[i])
    
    # Populate postfix array
    for i in range(1, len(nums)):
        postfixArray.append(postfixArray[-1]* nums[-i])
        
    # Reverse the postfix array
    postfixArray = postfixArray[::-1]
    for i in range(len(nums)):
        res.append(prefixArray[i]*postfixArray[i])
        
    return res
    
        
if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))
    print(productExceptSelf1([1,2,3,4]))
    print(productExceptSelf2([1,2,3,4]))




        