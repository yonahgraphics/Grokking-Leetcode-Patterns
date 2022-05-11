"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


# Time complexity: O(max(m, n)) where m, n are the lengths of the linked lists
# Space complexity: O(max(m, n)) where m, n are the lengths of the linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # compute sum
            v1 = l1.val if l1  else 0 # set the value to 0 if the list has ended
            v2 = l2.val if l2  else 0 # set the value to 0 if the list has ended
            
            
            # Get new carry
            totalOfValues = v1 + v2 + carry
            carry = totalOfValues//10
            totalOfValues = totalOfValues%10
                
            #Insert a new node in the result linkedList
            current.next = ListNode(totalOfValues)
            
            # update the pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
            