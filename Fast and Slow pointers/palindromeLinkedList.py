# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Time complexity O(n)
# Space complexity: O(n)
def isPalindrome(head):
    curr =  head
    nodes_values = []
    while curr is not None:
        nodes_values.append(curr.val)
        curr = curr.next
    
    # Two pointer approach
    i, j = 0, len(nodes_values)-1
    while i < j:
        if nodes_values[i] != nodes_values[j]:
            return False
        i += 1
        j -= 1
    return True
        
        