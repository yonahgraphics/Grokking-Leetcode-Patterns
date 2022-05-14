# Best Case Time complexity: O(nlogn) when our pivot happens to be the middle or close to middle of the array with one half 
# greater and another less than it. We go thru n elements at every level of a tree logn times, 
# because the tree will have logn levels

# Worst Case Time complexity: O(n^2). This happens when we get a sorted array or an array such as [2,2,2]
# Worst case scenerio can be avoided by using a randomized version of quicksort
# Inplace sorting algorithm
# Space complexity: O(1)
# Not a stable algorithm

# Python program for implementation of Quicksort Sort
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def quicksort(arr):
    qs(arr, 0, len(arr) - 1)

# function to perform quicksort
def qs(arr, l, r):
    if l >= r:
        return
    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    p = partition(arr, l, r)
    # recursive call on the left of pivot
    qs(arr, l, p - 1)
    # recursive call on the right of pivot
    qs(arr, p + 1, r)


# function to find the partition position
def partition(arr, l, r):
    # choose the rightmost element as pivot
    pivot = arr[r]
    # pointer for greater element
    i = l - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(l, r):
        if arr[j] < pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1
            # swapping element at i with element at j
            arr[i], arr[j] = arr[j], arr[i]
    # swap the pivot element with the greater element specified by i
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    # return the position from where partition is done
    return i + 1

a1 = [3, 2, 1]
a2 = [1, 2, 3]
a3 = []
a4 = [3, 1, -1, 0, 2, 5]
a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
a6 = [0]
a7 = [3, -2, -1, 0, 2, 4, 1]

quicksort(a1)
quicksort(a2)
quicksort(a3)
quicksort(a4)
quicksort(a5)
quicksort(a6)
quicksort(a7)

assert a1 == [1, 2, 3]
assert a2 == [1, 2, 3]
assert a3 == []
assert a4 == [-1, 0, 1, 2, 3, 5]
assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
assert a6 == [0]
assert a7 == [-2, -1, 0, 1, 2, 3, 4]

print("If you didn't get an assertion error, this program has run successfully.")