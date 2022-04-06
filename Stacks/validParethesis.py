"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

# Time complexity: O(n) because we traverse the entire string once
# Space complexity: O(n) because we use a map, and stack
def isValid(s):
    stack = []
    map = { ')': '(', '}':'{', ']':'['}
    
    for char in s:
        if char in map:
            if len(stack) > 0 and stack[-1] == map[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
        
    return len(stack) == 0


if __name__ == "__main__":
    print(isValid("(()"))
        