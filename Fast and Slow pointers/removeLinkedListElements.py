"""
203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of 
the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def removeElements(self, head, val):

        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next
          
