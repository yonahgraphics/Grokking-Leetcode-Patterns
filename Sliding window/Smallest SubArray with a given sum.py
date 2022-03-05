
# Given an array of positive numbers and a positive number ‘S,’ 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists

# Try problem: https://leetcode.com/problems/minimum-size-subarray-sum/
import math
def smallestSubarrayNaive(array, target): # O(n2)
    min_len = math.inf
    for i in range(len(array)):
        # Check for single numbers cuz a single number could be >=  the target
        sum = array[i]
        # len_count = 1
        if sum >= target:
            return 1

        for j in range(i+1, len(array)):
            sum += array[j]
            # len_count += 1 
            # Instead of using len_count, you could use j - i + 1
            if sum >= target:
                min_len = min(min_len, j - i +1)
                break
    return 0 if min_len == math.inf else min_len




'''
The time complexity of the above algorithm will be O(N). 
The outer for loop runs for all elements, 
and the inner while loop processes each element only once;
 therefore, the time complexity of the algorithm will be O(N+N)), 
 which is asymptotically equivalent to O(N).
The algorithm runs in constant space O(1).
'''
import math
def smallestSubarrayOptimum(array, S): # O(n)
    l, sum = 0, 0
    r = 0
    minima = math.inf
    
    for r in range(len(array)):
        sum += array[r]
        while sum >= S:
            minima = min(r-l + 1, minima)
            sum -= array[l]
            l += 1
    return 0 if minima == math.inf else  minima
      

if __name__ == "__main__":
    print(smallestSubarrayOptimum([1, 4, 7, 6, 9, 19], 20))
    print(smallestSubarrayNaive([1, 4, 7, 6, 9, 19], 20))
  
                
                

                
                
                
                
                