"""

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""


#Time complexity for get and put: O(1)

#Doubly Linkedlist node to store key-value pairs
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Cache = {} # Map the key to the node
        
        self.right      = Node(0,0)
        self.left       = Node(0,0)
        self.left.next  = self.right
        self.right.prev = self.left
        
    # Method to remove a node from LL
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    
    #Method to insert node into LL
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
       
          
    def get(self, key: int) -> int:
        if key not in self.Cache:
            return -1
        # Update LL to make it the most recently used
        self.remove(self.Cache[key])
        self.insert(self.Cache[key])
        return self.Cache[key].val
   
    def put(self, key: int, value: int) -> None:
        if key in self.Cache:
            self.remove(self.Cache[key])
            
        newNode = Node(key, value)
        self.Cache[key] = newNode
        self.insert(self.Cache[key])
            
        if len(self.Cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.Cache.pop(lru.key)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

