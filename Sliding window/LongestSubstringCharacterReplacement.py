
''''
The below algorithm’s time complexity will be O(N), 
where ‘N’ is the number of letters in the input string.
As we expect only the lower case letters in the input string, 
we can conclude that the space complexity will be O(26) to store 
each letter’s frequency in the HashMap, which is asymptotically equal to O(1).
'''
def characterReplacementNaive(s, k): # O(n) space, #O(n) time
        freq = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            # freq[s[r]] = freq.get(s[r], 0) + 1
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            
            while (r-l + 1) - max(freq.values()) > k: #The sort is klogk since we have atmost k+1 elements in the dict
                freq[s[l]] -= 1
                l += 1
                
            max_len = max((r-l + 1), max_len)
        return max_len


def characterReplacementOptimized(s, k): # O(n) space, #O(n) time
        freq = {}
        l = 0
        max_len = 0
        max_freq = 0
        for r in range(len(s)):
            # freq[s[r]] = freq.get(s[r], 0) + 1
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            max_freq = max(max_freq, freq[s[r]])
            
            while (r-l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                
            max_len = max((r-l + 1), max_len)
        return max_len
            
if __name__ == "__main__":
    print(characterReplacementNaive("Tommy", 2))
    print(characterReplacementOptimized('Tommy',2))