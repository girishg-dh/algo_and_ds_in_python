from advanced_data_structure.trie.trie_node import TrieNode

class Trie:
    def __init__(self):
        """
        Initializes a Trie data structure.
        """
        self.root = TrieNode() 
    def insert(self, word: str) -> None:
        """
        A function that inserts a word into a Trie data structure.

        Parameters:
            word (str): The word to insert into the Trie.

        Returns:
            None
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        A function that searches for a given word in a Trie data structure.

        Parameters:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word


    def search_prefix(self, prefix: str) -> bool:
        """
        Searches for a given prefix in the Trie data structure.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            bool: True if the prefix is found in the Trie, False otherwise.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
