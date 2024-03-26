from linked_list_nodes import LinkedListNode
from linked_list import LinkedList
from print_list import print_list_with_forward_arrow

def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1: 
        return lists[0].head
    if len(lists) == 2:
        return merge_two_lists(lists[0].head, lists[1].head)
    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    return merge_two_lists(left, right)

def merge_two_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data < l2.data:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


# Driver code
def main():
    inputlists = [[[21, 23, 42], [1, 2, 4]],
        [[11, 41, 51], [21, 23, 42]],
        [[2], [1, 2, 4], [25, 56, 66, 72]],
        [[11, 41, 51], [2], [2], [2], [1, 2, 4]],
        [[10, 30], [15, 25], [1, 7], [3, 9], [100, 300], [115, 125], [10, 70], [30, 90]]
    ]
    inp_num = 1
    for i in inputlists:
        print(inp_num, ".\tInput lists:", sep = "")
        ll_lists = []
        for x in i:
            a = LinkedList()
            a.create_linked_list(x)
            ll_lists.append(a)
            print("\t", end = "")
            print_list_with_forward_arrow(a.head)
            print()
        inp_num += 1
        print("\tMerged list: \n\t", end = "")
        print_list_with_forward_arrow(merge_k_lists(ll_lists))
        print("\n", "-"*100, sep = "")

if __name__ == "__main__":
    main()