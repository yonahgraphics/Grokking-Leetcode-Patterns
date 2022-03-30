'''
Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
Leetcode Link: https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Iteratively

#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None # To point to the previous node
        curr = head # To hold the current node
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        