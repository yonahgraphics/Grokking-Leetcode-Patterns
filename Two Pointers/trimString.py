'''
Given a string, trim it to remove any leading and trailing spaces.
Preserve the spaces btn the words themselves. 
Return the trimmed string

Example:
Input: " Today is a good day!"
Output: "Today is a good day!"
'''
# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1)
def trimStr(s):
    
    i = 0
    j = len(s) - 1
    while s[i] == ' ' and i < j:
        i += 1
    while s[j] == ' ' and i < j:
        j -= 1
    return s[i:j+1]

if  __name__ == "__main__":
    print(trimStr(" jd   mjjd"))