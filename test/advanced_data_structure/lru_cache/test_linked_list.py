import unittest
from linked_list import LinkedList, LinkedListNode

class TestMoveToHead(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.node1 = LinkedListNode(1)
        self.node2 = LinkedListNode(2)
        self.node3 = LinkedListNode(3)
        self.linked_list.insert_at_head(self.node3)
        self.linked_list.insert_at_head(self.node2)
        self.linked_list.insert_at_head(self.node1)

    def test_move_to_head_with_existing_node(self):
        self.linked_list.move_to_head(self.node2)
        self.assertEqual(self.linked_list.get_head(), self.node2)

    def test_move_to_head_with_head_node(self):
        self.linked_list.move_to_head(self.node1)
        self.assertEqual(self.linked_list.get_head(), self.node1)

    def test_move_to_head_with_tail_node(self):
        self.linked_list.move_to_head(self.node3)
        self.assertEqual(self.linked_list.get_head(), self.node3)

    def test_move_to_head_with_none_node(self):
        self.linked_list.move_to_head(None)
        self.assertNotEqual(self.linked_list.get_head(), None)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()