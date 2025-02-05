class TrieNode:
    def __init__(self):
        #Each node stores children in a dictionary
        #Keys are characters, values are TrieNode reference
        self.children = {}
        #is_end marks if a complete word ends at this node
        self.is_end= False

class Trie:
    
    def __init__(self):
        #The trie always has a root node (empty node).
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            # If the character is not present, create a new node.
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of word.
        node.is_end = True
        
    def search(self, word):
        """Return True if word is in the trie, else False."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def search(self, word):
        """Return True if word is in the trie, else False."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix):
        """Return True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
# Example usage:
if __name__ == "__main__":
    trie = Trie()
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("heaven")
    trie.insert("goodbye")

    print(trie.search("hello"))    # Output: True
    print(trie.search("hel"))      # Output: False
    print(trie.startsWith("he"))   # Output: True
    print(trie.startsWith("goo"))  # Output: True
    print(trie.search("good"))     # Output: False