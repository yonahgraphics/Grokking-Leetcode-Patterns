def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            min_val = left[i]
            i += 1
        else:
            min_val = right[j]
            j += 1
        result.append(min_val)
    
    if i < len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])

    return result

def mergeSort(array):
    size = len(array)
    if len(array) <= 1:
        return array

    mid = size//2
    left = array[:mid]
    right = array[mid:]

 # Recursive call on each half
    sortedLeftHalf =  mergeSort(left)
    sortedRightHalf = mergeSort(right)
    return merge(sortedLeftHalf, sortedRightHalf)


if __name__ == "__main__":
    print(mergeSort([9, 16, 7, 1, 5, 2, 3]))