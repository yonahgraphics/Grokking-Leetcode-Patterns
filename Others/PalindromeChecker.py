# Given a string that can contain aphabets and non-aphabets, return True if the string is a palindrome and False if it's not. Ignore non-aphabets and case
# E.g Bob12, 124(lol23 are palindromes

def palChecker(s): # (n)
    """
    1. Initialize left and right pointer
    2. while the left is less than the right
        check if the value at left pointer is not an alphabet and ignore it
        do the same for the value at right pointer
    3. Check if the value at the left pointer and the right pointer are the same
    ignoring case
    
    if True:
        increment the left and decrement the right
    if not:
      return False
    if the loop ends:
        return true
    """
    l = 0
    r = len(s)-1
    
    while l < r:
        if not s[l].isalpha():
            l += 1
            continue
        if not s[r].isalpha():
            r -= 1
            continue
        if s[l].lower() == s[r].lower(): # O(1)
            l += 1
            r -= 1
        else:
            return False
    return True


def palCheckerNaive(s): # O(n)
    new_str = ""
    
    # Ignore non alphabets
    for c in s:
         if c.isalpha():
             new_str += c
    s_reversed = new_str[::-1]
    return s_reversed.lower() == new_str.lower()

if __name__ == "__main__":
    print(palChecker("Bob"))
    print(palCheckerNaive("1Bob"))
    
            
        
    