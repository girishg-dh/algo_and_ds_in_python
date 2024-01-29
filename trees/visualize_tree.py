def visualize_tree(root):
    """
    Generates a visual representation of a binary tree using ASCII art.

    :param root: The root node of the binary tree.
    :return: A string containing the ASCII art representation of the tree.
    """

    if root is None:
        return "\n"

    width = get_max_width(root)
    rows = get_rows(root, width)

    tree = ""
    for row in rows:
        for node in row:
            if node is not None:
                tree += f"{node.data} "
            else:
                tree += "  "
        tree += "\n"

    return tree

def get_max_width(node):
    """
    Returns the maximum width of the binary tree.

    :param node: The root node of the binary tree.
    :return: The maximum width of the tree.
    """

    if node is None:
        return 0

    left_width = get_max_width(node.left)
    right_width = get_max_width(node.right)
    return max(left_width, right_width) + 2

def get_rows(node, width):
    """
    Generates a list of rows containing the nodes of the binary tree.

    :param node: The root node of the binary tree.
    :param width: The width of each row.
    :return: A list of rows containing the nodes of the tree.
    """

    if node is None:
        return []

    left_rows = get_rows(node.left, width // 2)
    right_rows = get_rows(node.right, width // 2)

    current_row = []
    left_offset = 0
    for row in left_rows:
        for i, value in enumerate(row):
            current_row.append(None if value is None else value)
            left_offset += 1

    current_row.append(node)

    right_offset = 1
    for row in right_rows:
        for i in range(len(row)):
            current_row.append(None if row[i] is None else row[i])
            right_offset += 1

    return current_row

