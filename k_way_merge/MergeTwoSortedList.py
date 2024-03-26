from linked_list_nodes import LinkedListNode
from linked_list import LinkedList
from print_list import print_list_with_forward_arrow



def merge_two_lists(head1: LinkedListNode, head2: LinkedListNode) -> LinkedListNode:
    """_summary_

    Args:
        head1 (LinkedListNode): _description_
        head2 (LinkedListNode): _description_

    Returns:
        LinkedListNode: _description_
    """
    dummy = LinkedListNode(-1)
    prev = dummy
    while head1 and head2:
        if head1.data <= head2.data:
            prev.next = head1
            head1 = head1.next

        else:
            prev.next = head2
            head2 = head2.next
        prev = prev.next
    if head1:
        prev.next = head1
    elif head2:
        prev.next = head2
    return dummy.next



def main():
    input = (
        [[1, 2, 3],[1, 2, 3]],
        [[25, 33, 99], [1]],
        [[], [1]],
        [[-77, 0, 5], [1, 2, 7]],
        [[], []],
    )

    for i in range(len(input)):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.create_linked_list(input[i][0])
        list2.create_linked_list(input[i][1])

        print(i+1, ".\tInput: ")
        print("\t", end = " ")
        print_list_with_forward_arrow(list1.head)
        print("\n\t", end = " ")
        print_list_with_forward_arrow(list2.head)
        print("\n\n\tOutput: ")
        print("\t", end = " ")

        merged = merge_two_lists(list1.head, list2.head)
        print_list_with_forward_arrow(merged)
        print("\n", "-"*100)

if __name__ == "__main__":
    main()