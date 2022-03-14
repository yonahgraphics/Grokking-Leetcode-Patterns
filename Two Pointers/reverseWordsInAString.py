'''
151. Reverse Words in a String
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between 
two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverseWords(s):
    s = s.split()
    return " ".join(s[::-1])

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverseWords1(s):
    result = ""
    i = 0
    while True:
        while i < len(s) and s[i] == ' ':
            i += 1
        if i >= len(s):
            break
        j = i+ 1
        while  j < len(s) and s[j] != ' ':
            j += 1
        sub = s[i:j]
        if result == "":
            result = result + sub
        else:
            result = sub + " " + result
        
        i = j + 1
        
    return result


if __name__ == "__main__":
    print(reverseWords("  Happy Birthday To You! "))
    print(reverseWords1(" How old are you now?    "))