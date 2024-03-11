'''
Statement
Given two strings, ransom_note and magazine, check if ransom_note can be constructed using the letters from magazine.
Return TRUE if it can be constructed, FALSE otherwise.
'''
from collections import Counter

def can_construct(ransom_note, magazine):
    r, m = Counter(ransom_note), Counter(magazine)
    return r <= m

print(can_construct("baad", "abcd"))
print(can_construct("bad", "abcd"))
print(can_construct("code", "abcodf"))
print(can_construct("program", "rpgoarm"))


print(can_construct("codinginterviewquestions", "aboincsdefoetingvqtniewonoregessnutins"))
