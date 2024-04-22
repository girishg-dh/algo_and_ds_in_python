class LinkedListNode:
    def __init__(self, pair):
        """
        Initializes a new instance of the LinkedListNode class.

        Parameters
        ----------
        pair : tuple
            A tuple containing two elements representing the first and second values of the node.

        Returns
        -------
        None

        """
        self.pair = pair
        self.first = pair[0]
        self.second = pair[1]
        self.next = None
        self.prev = None