"""
Link: https://leetcode.com/problems/linked-list-cycle/
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow, fast =  head, head # Initialize the pointers
        
        while fast is not None and fast.next is not None: # while fast has not reached the end (if no cycle) and fast.next is not None
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # Once they meet, we know there's a cycle
                return True
        return False # Otherwise, there's no cycle
            
            
