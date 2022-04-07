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
        


#Time complexity O(n)
# Space complexity: O(1)
def isPalindrome(self, head):
    # Find the middle of the linkedList
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Reverse a portion of a the linkedList
    prev = None
    curr = slow
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # Compare the values and check for palindrome
    while prev is not None:
        if prev.val != head.val:
            return False
        head = head.next
        prev = prev.next 
    return True
    
    