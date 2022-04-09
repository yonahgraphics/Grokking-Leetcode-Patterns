"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that 
each element appears only once. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
def deleteDuplicates(self, head):
    if head is None:
        return None
    
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    
    curr = head
    curr = curr.next
    prev = prev.next
    while curr:
        if curr.val == prev.val:
            prev.next = curr.next 
            curr = curr.next
        else:
            curr = curr.next
            prev = prev.next
        
    return dummy.next
    