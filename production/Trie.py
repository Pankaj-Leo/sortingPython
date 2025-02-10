class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_end_0f_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert (self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children [ch]
        node.is_end_of_node = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            return node.is_end_of_node

    def starts_with (self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
            return True

    def delete(self, s):
        def rec(node, s, i): #boolean recursive function
            if i == len(s): # checking if reached last node of the word to be deleted
                node.is_end = False # set the end of word as false
                return len(node.children) == 0  # Can delete this node if no children

            ch = s[i]
            if ch not in node.children:
                return False  # Word does not exist

            next_deletion = rec(node.children[ch], s, i + 1)
            if next_deletion:
                del node.children[ch]  # Remove child reference

            return next_deletion and not node.is_end and len(node.children) == 0


trie = Trie()
trie.insert("apple")
trie.insert("app")

print("Search apple:" , trie.search("apple")) #true
print("Starts with app: ", trie.starts_with("ap")) #true 2

trie.delete ("apple")
print("Search apple after deletion:", trie.search("apple")) # false
print("Search app after deletion:", trie.search("app")) # true