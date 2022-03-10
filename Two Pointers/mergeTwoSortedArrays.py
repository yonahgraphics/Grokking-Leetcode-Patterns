def mergeSortedArrays(arr1, arr2):
    i, j = 0, 0
    res = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
        if i >= len(arr1) and j < len(arr2):
            res.extend(arr2[j:])
            return res
        if j >= len(arr2) and i < len(arr1):
            res.extend(arr1[i:])
            return res
    return res
    
if  __name__ == "__main__":
    print(mergeSortedArrays([1,2], [2,3,4]))
        