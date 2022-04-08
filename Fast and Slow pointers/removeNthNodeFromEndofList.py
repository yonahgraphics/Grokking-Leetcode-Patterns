"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n)
# Space complexity: O(1)
def removeNthFromEnd(head, n):
# Count the number of nodes in the list.
# Get index of target node from start
# Remove it and return head
    num_nodes = 0
    curr = head
    while curr is not None:
        num_nodes += 1
        curr = curr.next
    target_index = num_nodes - n
    
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    
    counter = 0
    curr = head
    while curr is not None:
        if counter == target_index:
            prev.next = curr.next
            return dummy.next
        
        curr = curr.next
        prev = prev.next
        counter += 1
    return dummy.next
            
                
        
        
        
    
       
        