class BinarySearch:


    def __init__(self, search_space) -> None:
        self.search_space = search_space
    
    def search(self, value_to_find)-> bool:
        l, r = 0 , len(self.search_space)
        while(l < r):
            mid = (l + r)//2
            if value_to_find == self.search_space[mid]:
                return True
            elif value_to_find > self.search_space[mid]:
                l = mid
            else:
                r = mid
        return False

if __name__ == '__main__':
    a = BinarySearch([0,1,11,111,113,201,1001, 1003, 1105])
    print(a.search(1101))



    
