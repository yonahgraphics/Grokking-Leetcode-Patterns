"""
57. Insert Interval
You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the 
ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents 
the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
"""
# Approach 1
# You can just append the newInterval to intervals sort and then merge
# Time complexity: O(nlogn) due to sorting 
# Space complexity: O(n)
 


# Approach 2
# Since we are told that the list is sorted, we can find where the newInterval lies
# insert it and then merge as usual without sorting
# Time complexity: O(n)
# Space complexity: O(n)
def insert(self, intervals, newInterval):
    
    interval_len = len(intervals)
    if len(intervals) == 0:
        return [newInterval]
    
    # If the newInterval falls in the middle
    for idx, interval in enumerate(intervals):
        if interval[0] > newInterval[0]:
            intervals.insert(idx, newInterval)
            break   
    # If the new interval is at the beginning or at the end
    if len(intervals) == interval_len:
        if newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
        else:
            intervals.append(newInterval)
            
    # Merge intervals as usual    
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > res[-1][1]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(res[-1][1], intervals[i][1]) 
    return res