"""
Write a function to delete a node in a singly-linked list. You will not be given 
access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time complexity: O(1)
# Space complexity: O(1)
def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    # Since we don't have access to the node before the node we want to delete
    # we can copy the val of the next node to our target node into our target node
    # then delete the next node
    node.val = node.next.val # Copy data from next node into target node
    node.next = node.next.next # Delete target node
        
        