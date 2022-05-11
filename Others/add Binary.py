"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""
# Time complexity: O(max(n, m)), where n and m are the lengths of the two string
# Space complexity: O(1)
def addBinary(a, b):
        carry = 0
        totalStr = ""
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            v1 = a[i] if i >= 0 else 0
            v2 = b[j] if j >= 0 else 0
            
            #Compute the sum and new carry
            total = int(v1) + int(v2) + carry
            carry = total//2
            total = total%2
            totalStr = str(total) + totalStr
            
            #Update the pointers
            i -= 1
            j -= 1
            
        return totalStr
    
print(addBinary("11", "11"))