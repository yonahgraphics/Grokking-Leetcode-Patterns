"""
This algorithm is used to find the Kth largest/smallest element in the array
Best case: O(n)
Worst case: O(n^2)
"""

def qs(arr, l, r, k):
    p = partition(arr, l, r)
    if (k-1) == p:
        return arr[p]
    elif (k-1) > p:
        return qs(arr, p + 1, r, k)
    else:
        return qs(arr, l, p - 1, k)

def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
    
a1 = [3, 2, 1]
a2 = [1, 2, 3]
a3 = [3, 1, -1, 0, 2, 5]

# 2nd smallest element
result = qs(a3, 0, len(a3) - 1, 2)
print(result)
