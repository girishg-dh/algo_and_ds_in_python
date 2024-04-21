from advanced_data_structure.trie.trie import Trie
from advanced_data_structure.trie.trie_node import TrieNode


def main():
    keys = ["the", "a", "there", "answer", "xyz", "any", "by", "bye", "their"]
    trie_for_keys = Trie()
    num = 1
    for x in keys:
        print(num, ".\tInsert key: '", x, "'", sep="")
        trie_for_keys.insert(x)
        num += 1
        print("-" * 100)

    search = ["a", "answer", "xyz", "an", "the", "any", "by", "bye", "their", "abc"]
    for y in search:
        print(num, ".\tSearch key: '", y, "'", sep="")
        print("\tKey found? ", trie_for_keys.search(y), sep="")
        num += 1
        print("-" * 100)

    searchPrefix = ["b", "an"]
    for z in searchPrefix:
        print(num, ".\tSearch prefix: '", z, "'", sep="")
        print("\tPrefix found? ", trie_for_keys.search_prefix(z), sep="")
        num += 1
        print("-" * 100)


if __name__ == "__main__":
    main()