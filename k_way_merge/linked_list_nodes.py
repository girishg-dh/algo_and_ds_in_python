# Template for linked list node class
"""Class to create linked list node
"""
class LinkedListNode:
  # __init__ will be used to make a LinkedListNode type object
  def __init__(self, data, next=None):
    self.data = data
    self.next = next