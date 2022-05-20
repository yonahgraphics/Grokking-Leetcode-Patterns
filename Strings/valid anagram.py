
# Aproach1: Count Character frequency using a Hashmap
# Time complexity: O(m + n) where m & n are the lengths of strings s and t
# Space complexity: O(m + n)
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    charToCountForS = {}
    charToCountForT = {}
    
    for char in s:
        charToCountForS[char] = 1 + charToCountForS.get(char, 0)
    for char in t:
        charToCountForT[char] = 1 + charToCountForT.get(char, 0)
        
    for key in charToCountForS:
        if charToCountForS[key] != charToCountForT.get(key, 0):
            return False
        return True

# Aproach2: Sort the strings
# Time complexity: O(m+n)log(m + n) where m & n are the lengths of strings s and t
# Space complexity: O(1) using quick sort
def isAnagram1(s, t):
    return len(s) == len(t)


print(isAnagram1("boy", "boy"))