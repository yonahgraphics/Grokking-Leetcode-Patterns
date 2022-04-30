"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining. 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

# Approach 1
#Precalculating maxLeft and MaxRight for every element in the height array
# Then using the formular min(maxLeft, maxRight) - height[i]
# Add adding every postive result we get

# Time complexity: O(n) + O(n) + O(n) = 3*O(n) === O(n) 
# Space complexity: O(n) + O(n) === O(n)
def trap(height):
    maxLeftArray  = [0]
    maxRightArray = [0]
    trappedWater = 0
    
    # Populate maxRightArray
    for i in range(len(height)-1):
        maxLeft = max(height[i], maxLeftArray[-1])
        maxLeftArray.append(maxLeft)
        
    #Populate maxLeftArray
    for i in range(1, len(height)):
        maxLeft = max(height[-i], maxRightArray[-1])
        maxRightArray.append(maxLeft)
    
    #Reverse the maxRightArray because it is not in the right order
    maxRightArray = maxRightArray[::-1]
    
    # Now do iterate over the height array for the last time to sum trapped water
    for i in range(len(height)):
        currTrapped = min(maxLeftArray[i], maxRightArray[i]) - height[i]
        if currTrapped > 0:
            trappedWater += currTrapped
    return trappedWater

# Approach 2
# Time complexity: O(n) 
# Space complexity: O(1) 
def trap1(height):
        left = 1
        right = len(height)-2
        maxLeft = height[0]
        maxRight = height[-1]
        trappedWater = 0
        
        while left <= right: # While the pointers have not met
            if maxLeft < maxRight: # chose the water leve (min)
                maxLeft = max(maxLeft, height[left]) # update to avoid negatives when we subtract
                curr_trapped = maxLeft - height[left] # Get the trapped water at the current block
                trappedWater += curr_trapped          #Update the water volume
                left += 1                             #Move the pointer one step to the right
            else: # Do the same thing for on the right in the else case
                maxRight = max(maxRight, height[right])
                curr_trapped = maxRight - height[right]
                trappedWater += curr_trapped
                right -= 1
        return trappedWater

if __name__ == "__main__":
    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap1([0,1,0,2,1,0,1,3,2,1,2,1]))