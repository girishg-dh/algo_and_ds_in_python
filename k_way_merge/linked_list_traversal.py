
from linked_list_nodes import LinkedListNode
def traverse_linked_list(head: LinkedListNode):
    """_summary_

    Args:
        head (LinkedListNode): _description_
    """
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt