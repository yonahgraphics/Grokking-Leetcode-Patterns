"""
Leetcode: https://leetcode.com/problems/employee-free-time/
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find out if there is a free interval that is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

This problem follows the Merge Intervals pattern. Let’s take the an example:
Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
One simple solution can be to put all employees’ working hours in a list and sort them on the start time.'
Then we can iterate through the list to find the gaps. Let’s dig deeper. 
Sorting the intervals of the above example will give us:

[1,3], [2,4], [6,8], [9,12]
We can now iterate through these intervals, and whenever we find non-overlapping intervals 
(e.g., [2,4] and [6,8]), we can calculate a free interval (e.g., [4,6]).
"""
# Time complexity: O(nlogn)
# Space complexity: O(n)
def employeeFreeTime(workTimes):
    workTimes.sort()
    temp = workTimes[0]
    freeTimes = []

    for i in range(1, len(workTimes)):
        if workTimes[i][0] >= temp[1]:
            freeTimes.append([temp[1],workTimes[i][0]])
        temp = workTimes[i]
    return freeTimes

if __name__ == "__main__":
    workTimes = [[1,3], [9,12], [2,4], [6,8]]
    print(employeeFreeTime(workTimes))

