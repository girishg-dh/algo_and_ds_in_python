from linked_list_nodes import LinkedListNode
def reverse_linked_list(head: LinkedListNode):
    """_summary_

    Args:
        head (LinkedListNode): _description_

    Returns:
        _type_: _description_
    """
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev