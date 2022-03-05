'''
https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array containing 0s and 1s, if you are allowed to 
replace no more than ‘k’ 0s with 1s, find the length of the
 longest contiguous subarray having all 1s.

This problem follows the Sliding Window pattern and is
 quite similar to Longest Substring with same Letters 
 after Replacement. The only difference is that, in the 
 problem, we only have two characters (1s and 0s) in the input arrays.

Following a similar approach, we’ll iterate through the 
array to add one number at a time in the window. 
We’ll also keep track of the maximum number of repeating 1s 
in the current window (let’s call it maxOnesCount). So at any time,
 we know that we can have a window with 1s repeating maxOnesCount time,
  so we should try to replace the remaining 0s. If we have more than ‘k’ 
remaining 0s, we should shrink the window as we are not allowed to replace
more than ‘k’ 0s.

The above algorithm’s time complexity will be O(N), where ‘N’ is the 
count of numbers in the input array.
The algorithm runs in constant space O(1).
'''


def longestOnesIII(nums, k):
    l = 0
    maxOnesCount = 0
    # You can also just use zero_count instead of 
    # maxOnesCount since you want to replace the zeros
    res = 0
    for r in range(len(nums)):
        if nums[r] == 1:
            maxOnesCount += 1
            
        while (r-l+1) - maxOnesCount > k: # If you used maxOnesCount, no need to subtract
            # You'd just say while zero_count > k
            if nums[l] == 1: # And this would check for zero_count
                maxOnesCount -= 1
            l += 1
        res = max((r - l + 1), res)
    return res


if __name__ == "__main__":
    print(longestOnesIII(([1,1,1,0,0,0]), 2))