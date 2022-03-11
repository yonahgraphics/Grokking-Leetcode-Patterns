class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
#Time complexity : O(n), where n is the key length.

#In each iteration of the algorithm, we either examine or 
# create a node in the trie till we reach the end of the key. 
# This takes only n operations.
# Space complexity : O(n).
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode() 
            curr = curr.children[char]
        curr.endOfWord = True
        
    # Time complexity : O(n) In each step of the algorithm 
    # we search for the next key character. 
    # In the worst case the algorithm performs mm operations.
    #Space complexity : O(1)
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.helper(0, self.root, word)

    def helper(self, j, root, word):
        curr = root
        for i in range(j, len(word)):
            char = word[i]
            if char == ".":
                for child in curr.children.values():
                    if self.helper(i+1, child, word):
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
                curr = curr.children[char]
        return curr.endOfWord
        
if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("word")
    answer = obj.search(".ord")
    print(answer)