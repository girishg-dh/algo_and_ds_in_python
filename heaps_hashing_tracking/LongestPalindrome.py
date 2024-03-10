'''
What is the length of the longest palindrome that you can make using the letters in a given string
Example :
string = “xyyyyxxz”
Ans: 7
'''
from collections import Counter
def longest_palindrome(s: str) -> int:
    frequency = Counter(s)
    palindrome_len = 0
    for v in frequency.values():
        palindrome_len += int(v/2)
    return palindrome_len * 2 + 1 if palindrome_len < len(s) else palindrome_len * 2

def main():
    inputs = ["sfbaisdugfiubasdjFSDLBJS", 'abccccdddeeeeeeff', 'cool', 'GooooooOOOOODdddD' , 'REaccaR' , 'AbcDeFGhAachDeFG']
    for item in inputs:
        print(longest_palindrome(item))

if __name__=="__main__":
    main()