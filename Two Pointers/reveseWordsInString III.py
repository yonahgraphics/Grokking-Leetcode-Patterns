
def reverseWords(s):
    result = ""
    
    i = 0
    while True:
        while i < len(s) and s[i] == ' ':
            i += 1
        j = i+ 1
        while  j < len(s) and s[j] != ' ':
            j += 1
        sub = s[i:j]
        
        if result == "":
            result += reverseStr(sub)
        else:
            result = result + " "  + reverseStr(sub)
        
        i = j + 1
        
        if i >= len(s):
            break
    return result

def reverseStr(word):
    i = 0
    j = len(word)-1
    word = list(word)
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    return "".join(word)
    
    
if __name__ == "__main__":
    print(reverseWords("   Hello    everybody"))