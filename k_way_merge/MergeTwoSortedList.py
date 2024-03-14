from linked_list.linked_list import LinkedList
from linked_list.linked_list_node import LinkedListNode
from linked_list.print_list import print_list_with_forward_arrow






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