"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Approach 1
#iterate over the list, put the nodes into an array, sort them and create the list again
# Time complexity: O(nlogn)
# Space complexity: O(n)


# Aproach 2: Use Merge sort
# Time complexity: O(nlogn)
# Space complexity: O(logn) due to recursive calls
def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    fast = slow.next
    slow.next = None
    
    leftList  = self.sortList(head)
    rightList = self.sortList(fast)
    return self.merge(leftList, rightList)

def merge(self, list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
    return dummy.next
    
        
    