# Brute Force Approach
# Sorry, but it wouldn't work because the time complexity is O(n^3)!
class Solution:
    def isPali(self, st):
        if st == st[::-1]:
            return True
        return False

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if len(words) < 1:
            return []
        res = []
        l = len(words)
        for i in range(l):
            for j in range(i+1, l):
                temp = words[i]+words[j]
                if self.isPali(temp):
                    res.append([i, j])
                temp = words[j]+words[i]
                if self.isPali(temp):
                    res.append([j, i])
        return res

# Optimal Approach
# Time: O(n*m), where n is the length of the wordlist and m is the length of each word!
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup = {wrd[::-1]: idx for idx, wrd in enumerate(words)}
        res = []
        for idx, wrd in enumerate(words):
            for j in range(len(wrd)+1):
                pre, pos = wrd[:j], wrd[j:]
                if not len(pre) == 0 and pre == pre[::-1] and pos in lookup and lookup[pos] != idx:
                    res.append([lookup[pos], idx])
                if pos == pos[::-1] and pre in lookup and lookup[pre] != idx:
                    res.append([idx, lookup[pre]])
        return res