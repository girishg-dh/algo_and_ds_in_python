from heapq import *
class MaxHeap:
    def __init__(self) -> None:
        self.heap_list = []

    def insert(self, x):
        heappush(self.heap_list, -x)

    def get_top(self):
        return -self.heap_list[0]

    def __str__(self) -> str:
        out = '['
        for i in self.heap_list:
            out = out + str(-i)+', '
        out = out[:-2]+']'
        return out