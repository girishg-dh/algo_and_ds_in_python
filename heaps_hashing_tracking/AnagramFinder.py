'''Given two strings, a and b, return an array of all the start indexes of anagrams of b in a. 
We may return the answer in any order
abcda
ab
'''
from collections import Counter

def find_anagrams(a:str , b: str)-> list:
    result = []
    if len(b) > len(a):
        return result
    search_map = Counter(b)
    for idx in range(0, len(a)-len(b)+1):
        span_map = Counter(a[idx:idx + len(b)])
        if search_map == span_map:
            result.append(idx)
    return result

def main():
  A = ["abab", "cbaebabacd", "cefecf", "hello", "bro"]
  B = ["ab", "abc", "efc", "olleh", "bro"]
  for i in range(len(A)):
    print(i + 1, ".\tString a: \"", A[i], "\"", sep = "")
    print("\tString b: \"", B[i], "\"", sep = "")
    print("\tAnagrams of string b start at index(es) ", find_anagrams(A[i],B[i]), " in string a.", sep = "")
    print("-" * 100)

if __name__ == '__main__':
  main()