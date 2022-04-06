"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return 
null.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that 
pos is not passed as a parameter.

Do not modify the linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else: # Else statement only executed if the loop didn't end due to the break statement
            return None
        
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
            
        return fast 