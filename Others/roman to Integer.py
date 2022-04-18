"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# The trick is to keep the char to int mapping in a hasmap,
#  and then compare two consecutive chars. If the first is less than the next, subtract it
# else, add it
# Time Complexity: O(n)
# Space Complexity: O(1) since the hasmap size doesn't grow with input size
def romanToInt(s):
    intNum = 0
    
    if len(s) == 0:
        return 0
    map = {
            'I'   :1,
            'V'   :5,
            'X'   :10,
            'L'   :50,
            'C'   :100,
            'D'   :500,
            'M'   :1000
            }
    
    for i in range(1, len(s)):
        if map[s[i]] > map[s[i-1]]:
            intNum -= map[s[i-1]]
        else:
            intNum += map[s[i-1]]
        
    intNum += map[s[len(s)-1]]
    return intNum


if __name__ == "__main__":
    print(romanToInt("III"))