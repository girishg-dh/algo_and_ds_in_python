class TrieNode:
    """
    TrieNode is a node in a Trie data structure.

    Attributes:
        children: A dictionary that maps each character to a TrieNode.
            This represents the children of this node in the Trie.
        is_word: A boolean that indicates whether this node is the end of a word.
    """

    def __init__(self):
        """Creates a new TrieNode."""
        self.children = dict() # Dictionary that maps each character to a TrieNode
        self.is_word = False # Whether this node is the end of a word
