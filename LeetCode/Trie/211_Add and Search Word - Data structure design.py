class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.trie
        for letter in word:
            if letter not in curr:
                curr[letter] = dict()
            curr = curr[letter]
        curr['is_end'] = 1

    def search_helper(self, s, root, idx):
        if idx == len(s):
            return root.get('is_end') == True
        curr_char = s[idx]
        if curr_char != '.':
            if curr_char not in root:
                return False
            child_node = root[curr_char]
            return self.search_helper(s, child_node, idx + 1)
        for child_key in root:
            if child_key != 'is_end':
                child_node = root[child_key]
                if self.search_helper(s, child_node, idx + 1):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.trie, 0)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
obj.addWord("bat")

print(obj.search("b."))

