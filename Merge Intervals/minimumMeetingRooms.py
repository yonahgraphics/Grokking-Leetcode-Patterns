def minimumMeetingRooms(intervals):
    intervals.sort()
    temp = intervals[0]
    
    num_rooms = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] < temp[1]:
            num_rooms += 1
        temp = intervals[i]
    return num_rooms

if __name__ == "__main__":
    intervals = [[4,5], [2,3], [2,4], [3,5]]
    print(minimumMeetingRooms(intervals))
# times [[4,5], [2,3], [2,4], [3,5]]
# sorted Times [[2,3], [2,4], [3,5], [4,5]]

# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

#temp = [2,3]