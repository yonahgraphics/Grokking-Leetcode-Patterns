"""
Leetcode:https://leetcode.com/problems/meeting-rooms/

Given an array of intervals representing ‘N’ appointments, find out if a person 
can attend all the appointments.

The problem follows the Merge Intervals pattern. We can sort all the intervals by 
start time and then check if any two intervals overlap. A person will not be able to attend all appointments if any two appointments overlap.
"""
def canAttendAllAppointments(meetings):
    meetings.sort()
    temp = meetings[0]

    for i in range(1, len(meetings)):
        if meetings[i][0] <= temp[1]:
            return False
        temp = meetings[i]
    return True


if __name__ == "__main__":
# canAttendAllAppointments([[1,4], [2,5], [7,9]])//false, Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# canAttendAllAppointments([[6,7], [2,4], [8,12]])//true, None of the appointments overlap, therefore a person can attend all of them.
# canAttendAllAppointments([[4,5], [2,3], [3,6]])//false, Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
    print(canAttendAllAppointments([[1,4], [2,5], [7,9]]))
    print(canAttendAllAppointments([[6,7], [2,4], [8,12]]))
    print(canAttendAllAppointments([[4,5], [2,3], [3,6]]))