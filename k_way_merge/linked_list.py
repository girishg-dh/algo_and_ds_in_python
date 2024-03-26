from linked_list_nodes import LinkedListNode

# Template for the linked list
class LinkedList:
    
    # __init__ will be used to make a LinkedList type object
    def __init__(self):
        self.head = None
    
    # insert_node_at_head method will insert a LinkedListNode at head of a linked list
    def insert_node_at_head(self, node):
        """_summary_

        Args:
            node (_type_): _description_
        """
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create_linked_list method will create the linked list using the given 
    # integer array with the help of InsertAthead method
    def create_linked_list(self, lst):
        """_summary_

        Args:
            lst (_type_): _description_
        """
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result