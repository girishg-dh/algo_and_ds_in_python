# Template for printing the linked list with forward arrows

def print_list_with_forward_arrow(linked_list_node):
    """_summary_

    Args:
        linked_list_node (_type_): _description_
    """
    temp = linked_list_node
    if not temp:
        print("None", end=" ")
    while temp:
        print(temp.data, end=" ") # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            print("→ null", end=" ") # if this is the last node, print null at the end