'''
56. Merge Intervals (Medium)

Leetcode link: https://leetcode.com/problems/merge-intervals/
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping 
intervals, and return an array of the non-overlapping intervals that cover all the 
intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# Time complexity: O(nlogn) due to sorting
#In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space 
#complexity of O(n)
# Space complexity: O(n) due to sorting
def merge(intervals):
    #Sort the intervals according to the start time
    #intervals.sort() # O(nlogn)
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    
    for i in range(1, len(intervals)): # O(n)
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1], result[-1][1])
        else:
            result.append(intervals[i])
    return result
        
        
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    #Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    #Output: [[1,6],[8,10],[15,18]]
    print(merge(intervals))