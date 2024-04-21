class Node:
    def __init__(self, data):
        self.data = data
        self.neighbours = []

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return str(self.data)