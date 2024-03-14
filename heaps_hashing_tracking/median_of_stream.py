from min_heap import *
from max_heap import *

class MedianOfStream:
    def __init__(self) -> None:
        self.maxheap = MaxHeap()
        self.minheap = MinHeap()

    def insert_num(self, num):
        #insert element based on current median
        if len(self.maxheap.heap_list) == 0:
            self.maxheap.insert(num)
        elif num > self.maxheap.get_top():
            self.minheap.insert(num)
        else:
            self.maxheap.insert(num)

        #adjust the size of the heaps
        if len(self.maxheap.heap_list) > len(self.minheap.heap_list) + 1:
            self.minheap.insert(-heappop(self.maxheap.heap_list))
        elif len(self.minheap.heap_list) > len(self.maxheap.heap_list):
            self.maxheap.insert(heappop(self.minheap.heap_list))

    def find_median(self):
        if (len(self.minheap.heap_list) + len(self.maxheap.heap_list)) % 2 == 0:
            return (self.maxheap.get_top() + self.minheap.get_top()) / 2
        else:
            return self.maxheap.get_top()







def main():
    median_num = MedianOfStream()
    nums = [35, 22, 30, 25, 1]
    numlist = []
    x = 1
    for i in nums:
        numlist.append(i)
        print(x, ".\tData stream: ", numlist, sep="")
        median_num.insert_num(i)
        print("\tThe median for the given numbers is: " +
              str(median_num.find_median()), sep="")
        print(100*"-"+"\n")
        x += 1


if __name__ == "__main__":
    main()