def twoSumIINaive(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Since we know that the array is sorted, 
# Use two pointers i and j at the end and 
# at the beginning of the array
# increment the i if the sum nums[i] + nums[j] is less than target
# increment decrement j if the sum nums[i] + nums[j] is greater than the target
def towSUmIITwoPointers(nums, target):
    i = 0
    j = len(nums) - 1
    while j > i:
        sum = nums[i] + nums[j]
        if sum == target:
            return [i,j]
        if sum > target:
            j -= 1
        if sum < target:
            i += 1

if __name__ == "__main__":
    print(twoSumIINaive([1,3,5,6], 7))
    print(towSUmIITwoPointers([1,3,5,6], 7))
            
    