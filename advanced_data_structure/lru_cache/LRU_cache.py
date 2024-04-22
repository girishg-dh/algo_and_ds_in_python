from advanced_data_structure.lru_cache.linked_list import LinkedList

# We will use a linkedlist of a pair of integers
# where the first integer will be the key
# and the second integer will be the value
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_map = {}
        self.cache = LinkedList()
    
    def get(self, key):
        found_item = None
        if key in self.cache_map:
            found_item = self.cache_map[key]
            self.cache.move_to_head(found_item)
            return found_item.pair[1]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache_map:
            found_item = self.cache_map[key]
            found_item.value = (key, value)
            self.cache.move_to_head(found_item)
            return

        if self.cache.get_size() == self.capacity:
            tail_item_key = self.cache.get_tail().pair[0]
            # Remove the tail item from the cache
            self.cache.remove_tail()
            # Remove the tail item from the cache map
            del self.cache_map[tail_item_key]
        # Add the new item to the cache
        self.cache.insert_at_head((key, value))
        # Add the new item to the cache map
        self.cache_map[key] = self.cache.get_head()
        return
    
    # Print the contents of the cache in fancy way and user friendly way
    def print(self):
        print("Cache current size: ", self.cache.size,
                ", ", end="")
        print("Cache contents: {", end="")
        node = self.cache.get_head()
        while node:
            print("{", str(node.pair[0]), ":", str(node.pair[1]),
                    "}", end="")
            node = node.next
            if node:
                print(" -> ", end="")
        print("}")
        print("-"*20, "\n")
        print("-" * 20)
