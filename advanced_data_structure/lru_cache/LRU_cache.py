from advanced_data_structure.lru_cache.linked_list import LinkedList

# We will use a linkedlist of a pair of integers
# where the first integer will be the key
# and the second integer will be the value
class LRUCache:
    def __init__(self, capacity):
        """
        Initializes the LRUCache object with the given capacity.

        Parameters:
            capacity (int): The maximum number of key-value pairs that the cache can hold.

        Returns:
            None
        """
        self.capacity = capacity
        self.cache_map = {}
        self.cache = LinkedList()
    
    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Parameters:
            key (Any): The key to retrieve the value for.

        Returns:
            int: The value associated with the key if it exists in the cache, otherwise -1.
        """
        found_item = None
        if key in self.cache_map:
            found_item = self.cache_map[key]
            self.cache.move_to_head(found_item)
            return found_item.pair[1]
        else:
            return -1

    def set(self, key, value):
        """
        Sets a key-value pair in the cache. If the key already exists in the cache, updates the corresponding value and moves the item to the head of the cache. If the cache is full, removes the least recently used item from the cache and the cache map. Adds the new item to the head of the cache and the cache map.

        Parameters:
            key (Any): The key to set in the cache.
            value (Any): The value to set in the cache.

        Returns:
            None
        """
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
        """
        Print the contents of the cache in a fancy way and a user-friendly way.
        
        This function prints the current size of the cache and the contents of the cache in a formatted way.
        It iterates over the cache and prints each key-value pair enclosed in curly braces. If there are multiple
        key-value pairs, they are separated by an arrow ("->"). The function also prints a line of hyphens ("-") 
        for visual separation.
        
        Parameters:
            self (LRUCache): The LRUCache object.
        
        Returns:
            None
        """
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
