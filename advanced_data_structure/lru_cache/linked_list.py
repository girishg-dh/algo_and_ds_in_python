from advanced_data_structure.lru_cache.linked_list_node import LinkedListNode

class LinkedList:
    # _init__ initialises the linked list type object
    def __init__(self):
        # head and tail will store the head and tail of the linked list
        self.head = None
        self.tail = None
        self.size = 0

    # move_to_head will move the given node to head
    def move_to_head(self, node):
        """
        To move the given node to the head of the linked list.
        If the provided node is None, return without any action.
        Delinks the node from its current position and updates the connections accordingly.
        If the node is the head or tail of the list, adjusts the head and tail pointers accordingly.
        Inserts the node at the head of the list if it's not empty.
        """
        # If node is None, return
        if not node:
            return
        # To move node to head delink it from its current position
        # To delink next node and connect it to previous node
        # Make previous node's next to current nodes next 
        if node.prev:
            node.prev.next = node.next

        # To move node to head delink it from its current position
        # Make next node's previous to current nodes previous
        if node.next:
            node.next.prev = node.prev
        
        # If node is head, set head to next node
        if node == self.head:
            self.head = self.head.next
        # If node is tail, set tail to previous node
        if node == self.tail:
            self.tail = self.tail.prev
            # if tail still exists, make None
            if self.tail:
                self.tail.next = None
        
        # Insertion at the head
        # Case 1: If linked list is empty, set head and tail to node
        if not self.head:
            self.head = node
            self.tail = node
        # Case 2: If linked list is not empty, 
        # set given node's next on top of head and head's previous to given node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # Insert_at_head will insert the given pair at head
    def insert_at_head(self, pair):
        """
        Inserts a new node with the given pair at the head of the linked list.

        Parameters:
            pair (tuple): A tuple containing the first and second values of the node.

        Returns:
            None
        """
        new_node = LinkedListNode(pair)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Insert_at_tail will insert the given pair at tail
    def insert_at_tail(self, pair):
        """Insert new node at the tail of the linked list."""
        new_node = LinkedListNode(pair)
        # If linked list is empty, set head and tail to new node
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        # If linked list is not empty, set new node's next to tail and tail's previous to new node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

     # get_head will return the head of the linked list
    def get_head(self):
        return self.head
    
     # get_tail will return the tail of the linked list
    def get_tail(self):
        return self.tail

     # get_size will return the size of the linked list
    def get_size(self):
        return self.size
    
    # remove_node will remove the given node from the LinkedList
    def remove_node(self, node):
        """
        Remove the given node from the LinkedList.

        Parameters:
            node: Node to be removed from the LinkedList.

        Returns:
            None
        """
        # If node is None, return
        if not node:
            return
        # To remove node, delink it from its current position
        if node.prev:
            node.prev.next = node.next
        # To delink next node and connect it to previous node
        if node.next:
            node.next.prev = node.prev
        # If node is head, set head to next node
        if node == self.head:
            self.head = self.head.next
        # If node is tail, set tail to previous node
        if node == self.tail:
            self.tail = self.tail.prev
            # if tail still exists, make None
            if self.tail:
                self.tail.next = None
        # Decrement size
        self.size -= 1
        # Delete node
        del node


    # remove_node will remove the given node from the LinkedList
    def remove(self, pair):
        """
        Removes a node from the linked list that contains the given pair.

        Parameters:
            pair (tuple): A tuple containing the first and second values of the node.

        Returns:
            None
        """
        # 
        i = self.get_head()
        while i:
            if i:
                self.remove_node(i)
                return
            i = i.next


    # remove_head will remove the head of the linked list
    def remove_head(self):
        return self.remove_node(self.head)

    # remove_tail will remove the tail of the linked list
    def remove_tail(self):
        return self.remove_node(self.tail)

    