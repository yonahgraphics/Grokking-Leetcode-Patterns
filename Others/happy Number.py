'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it 
loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
'''

#Aproach 1: Using a HashSet

# Time complexity: O(243⋅3+logn+loglogn+logloglogn)... = O(log n)
# Space complexity: O(logn)

# It is a measure of what numbers we're putting in the HashSet,
# and how big they are. 
# For a large enough n, the most space will be taken by n itself.
def isHappy(n):
    seen = set()
    
    while n != 1:
        
        sumOfSquares =  calculatSumOfSquares(n)   

        if sumOfSquares in seen:
            return False
        seen.add(sumOfSquares)
        n = sumOfSquares
    return True

def calculatSumOfSquares(n):
    sumOfSquares = 0 
    while n != 0:
        sumOfSquares += (n % 10)**2
        n = n // 10
    return sumOfSquares
                 

#Aproach 2: Using two pointers (Floyd's tortoise and hare)
# Time complexity: O(n)
# Space complexity: O(1)
def isHappy(n):
    slow = n
    fast = n
    
    while True:
        slow = calculatSumOfSquares(slow)
        fast = calculatSumOfSquares(calculatSumOfSquares(fast))
        if fast == 1 or fast == slow:
            break
    return fast == 1
        
def calculatSumOfSquares(n):
    sumOfSquares = 0 
    while n != 0:
        sumOfSquares += (n % 10)**2
        n = n // 10
    return sumOfSquares
                

