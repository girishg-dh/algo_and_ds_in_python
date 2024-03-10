'''
Given two words, src and dest, and a list, words, return the number of words in the shortest transformation sequence from src to dest.
If no such sequence can be formed, return 0
A transformation sequence is a sequence of words (src → word1 → word2 -> word3 -> wordj)
that has the following properties: wordj = dest
Every pair of consecutive words differs by a single character.
All the words in the sequence are present in the words. The src does not need to be present in words.
'''
from collections import deque
def word_ladder(src: str, dest: str, words: list) -> int:
    word_set = deque(words)
    ladder_counter = 0
    word_queue = deque()
    if dest not in word_set:
        return ladder_counter
    word_queue.append(src)
    while word_queue:
        left = word_queue.pop()
        temp_set = word_set.copy()
        for right in temp_set:
            if compare_words(left, right):
                word_queue.append(right)
                word_set.remove(right)
                if right == dest:
                    return ladder_counter + 1
        ladder_counter += 1
    return 0

def compare_words(left: str, right: str) -> bool:
    not_same_count = 0
    for idx in range(len(left)):
        if left[idx] != right[idx]:
            not_same_count += 1
    return not_same_count == 1


def main():
    srcs = ['hit', 'hit', 'hat', 'dog', 'dogs']
    dests = ['cog', 'cog', 'log', 'cat', 'frog']
    inputs = [
        ["hot","dot","lot","log","cog"],
        ["hot","dot","lot","log","com"],
        ["hot","not","dot","lot","cog"],
        ["hog","dot","pot","pop","mop","map","cap","cat"],
        ["play","jump","land","pack","cats","comb","pick"]
        ]

    for index in range(len(srcs)):
        print(word_ladder(srcs[index], dests[index], inputs[index]))

if __name__=="__main__":
    main()