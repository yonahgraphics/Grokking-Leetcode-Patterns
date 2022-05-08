# def minimumMeetingRooms(intervals):
#     intervals.sort()
#     currentInterval = intervals[0]
#     min_rooms = 1
    
#     for i in range(1, len(intervals)):
     
#         if intervals[i][0] <= currentInterval[1]:
#             min_rooms += 1
#             # min_rooms = min(min_rooms, current_rooms)
#         else:
#             currentInterval = intervals[i]
#     return min_rooms



def minimumMeetingRooms1(intervals):
    intervals.sort()
    temp = intervals[0]
    num_rooms = 1
    for i in range(len(intervals)):
        if intervals[i][0] < temp[1]:
            num_rooms += 1
        else:
            temp = intervals[i]
    return num_rooms




 

if __name__ == "__main__":
    intervals = [[4,5], [2,3], [2,4], [3,5]]
    # intervals = [[1,3], [2, 5], [4, 7]]
    # print(minimumMeetingRooms(intervals))
    print(minimumMeetingRooms1(intervals))
    
# times [[4,5], [2,3], [2,4], [3,5]]
# sorted Times [[2,3], [2,4], [3,5], [4,5]]

# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

#temp = [2,3]