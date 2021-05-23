class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char = ""
        self.is_end = False# whether this can be the end of a word
        self.counter = 0# a counter indicating how many times a word is inserted
        self.children = {} # a dictionary of child nodes (keys characters, values nodes)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of a word
        node.is_end = True
        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
