from collections import Counter

def is_anagram(left: str, right: str)-> bool:
    c1, c2 = Counter(left.lower()), Counter(right.lower())
    return c1 == c2


def main():
    left = ['anagram','spare','heart', 'super']
    right = ['nagaram','pears', 'earth', 'upper']
    for i, k in enumerate(left):
        print('{} and {} are{} anagrams'.format(left[i], right[i], "" if is_anagram(left[i], right[i]) else " not"))

if __name__=="__main__":
    main()
