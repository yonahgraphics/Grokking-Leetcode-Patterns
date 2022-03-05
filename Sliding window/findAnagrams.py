
def findAnagrams(s, p):
    if len(p) > len(s): return []
    
    pCount, sCount = [0]*26, [0]*26
    numMatches= 0
    l = 0
    
    anagram_idx = []
    
    for i in range(len(p)):
        pCount[ord(p[i]) - ord('a')] += 1
        sCount[ord(s[i]) - ord('a')] += 1

    for i in range(26):
        numMatches += (1 if pCount[i] == sCount[i] else 0)

    for r in range(len(p), len(s)):
        if numMatches == 26:
            anagram_idx.append(l)

        # Expand window
        index = ord(s[r]) - ord('a')
        sCount[index] += 1
        if pCount[index] == sCount[index]:
            numMatches += 1
        elif pCount[index] + 1 == sCount[index]:
            numMatches -= 1

        #Shrink window
        index = ord(s[l]) - ord('a')
        sCount[index] -= 1
        if pCount[index] == sCount[index]:
            numMatches += 1
        elif pCount[index] - 1 == sCount[index]:
            numMatches -= 1
        l += 1
    if numMatches == 26:
        anagram_idx.append(l)
    return anagram_idx


if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))

    