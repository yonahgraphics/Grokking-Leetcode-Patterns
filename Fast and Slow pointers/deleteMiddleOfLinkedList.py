""""
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
095. Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return the head 
of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start 
using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
def middleNode(head):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next
        prev.next = slow.next
        return dummy.next

