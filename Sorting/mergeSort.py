# Time: O(logn)
# Space: O(n)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    print(arr[mid])
    arrLeft = mergeSort(arr[:mid])
    arrRight = mergeSort(arr[mid:])
    return merge(arrLeft, arrRight)
    
def merge(arrLeft, arrRight):
        l, r = 0,0
        res = []
        while l < len(arrLeft) and r < len(arrRight):
            if arrLeft[l] < arrRight[r]:
                res.append(arrLeft[l])
                l += 1
            else:
                res.append(arrRight[r])
                r += 1
        if l < len(arrLeft):
            res.extend(arrLeft[l:])
        if r < len(arrRight):
            res.extend(arrRight[r:])
        return res
  
    
    
print(mergeSort([1, 7,2,0,3]))
    
