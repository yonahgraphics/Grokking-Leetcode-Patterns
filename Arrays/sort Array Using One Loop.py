"""
Given an un sorted array, sort it using just one loop
"""
# Time complexity: O(n^2)
# Space complexity: O(1)
def sort(arr):
    i = 0              
    while  i < len(arr)-1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i = -1
        i+= 1
    return arr
print(sort([1,4,2,4,6,2]))



