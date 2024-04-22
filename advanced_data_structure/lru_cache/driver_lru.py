from advanced_data_structure.lru_cache.LRU_cache import LRUCache
def main():
    # Creating a cache of size 2
    cache_capacity = 5
    cache = LRUCache(cache_capacity)
    print("Initial state of cache")
    print("Cache capacity: " + str(cache_capacity))
    cache.print()

    keys = []
    values = ["20", "get", "25", "40", "get", "85", "5"]

    for i in range(len(keys)):
        if values[i] == "get":
            print("Getting by Key: ", keys[i])
            print("Cached value returned: ", cache.get(keys[i]))
        else:
            print("Setting cache: Key: ", keys[i], " Value: ", values[i])
            cache.set(keys[i], int(values[i]))
        cache.print()


if __name__ == '__main__':
    main()
