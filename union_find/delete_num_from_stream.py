"""Successor with delete: Delete numbers and find a successor to a number in a stream of integers from 1 to n.
To delete numbers and find a successor to a number in a stream of integers from 1 to n efficiently, 
we can use a data structure like a set to keep track of the deleted numbers and a sorted list to maintain the remaining numbers. 
When we need to find a successor to a number, we can search for the next available number in the sorted list.
"""

import bisect # Pyhton library for maintaining a sorted list and doing binary search on them

class StreamSucessor:
    def __init__(self, n):
        self.deleted = set()
        self.is_available = list(range(1, n+1))
    def delete(self, num):
        if num not in self.deleted:
            bisect.insort(self.is_available, num)
            self.deleted.add(num)
    def successor(self, num):
        index = bisect.bisect_right(self.is_available, num)
        if index < len(self.is_available):
            return self.is_available[index]
        return None
    
def main():
    stream_successor = StreamSucessor(20)
    stream_successor.delete(2)
    stream_successor.delete(5)
    stream_successor.delete(7)
    print(f'Successor is:{stream_successor.successor(4)}')

if __name__ == '__main__':
    main()