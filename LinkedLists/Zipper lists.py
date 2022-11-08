# Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
# The function should zipper the two lists together into single linked list by alternating nodes.
# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
# The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

#-------------------------------------------------------------------------------------------
# Example
# a -> b -> c -> d -> e -> f
# x -> y -> z

#output
# a -> x -> b -> y -> c -> z -> d -> e -> f

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zipper_lists(head_1, head_2):
  dummy = Node(0)
  tail = dummy

  curr1, curr2 = head_1, head_2
  while curr1 and curr2:
    tail.next = curr1
    curr1 = curr1.next
    tail = tail.next
    tail.next = curr2
    curr2 = curr2.next
    tail = tail.next
  if curr1:
    tail.next = curr1
  if curr2:
    tail.next = curr2
  return dummy.next
