
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Similar problem to try: https://leetcode.com/problems/maximum-average-subarray-i/

def averageNaive(array, k): # O(nk)
    i = 0
    avgs = []
    while i <= len(array)-k:
        subArray= array[i:i+k]
        sum = 0
        for num in subArray:
            sum += num
        avg = sum/k
        avgs.append(avg)
        i += 1
    return avgs
    
'''
The efficient way to solve this problem would be to visualize each contiguous
 subarray as a sliding window of ‘5’ elements. This means that we will slide 
 the window by one element when we move on to the next subarray. 
 To reuse the sum from the previous subarray, we will subtract the element 
 going out of the window and add the element now being included in the sliding window.
This will save us from going through the whole subarray to find the sum and, 
as a result, the algorithm complexity will reduce to O(N).
'''
def averageOptimum(array, k):# O(n)
    i= 0
    j = k
    subArray = array[i:k]
    sum = 0
    for num in subArray:
        sum += num
    Avgs = [sum/k]
  
    while j < len(array): # O(n/k)= O(n) + O(k)
        sum = (sum + array[j]) - array[i]
        new_avg = sum/k
        Avgs.append(new_avg)
        i += 1
        j += 1
    return Avgs
    
if __name__ == "__main__":
    print(averageNaive([1,2,3,4,5], 2))
    print(averageOptimum([1,2,3,4,5], 2))
    

    
        
   
    
