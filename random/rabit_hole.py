"""
You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia.
The encyclopedia consists of N different web pages, numbered from 1 to N. Each page i contains nothing but a 
single link to a different page Li.
A session spent on this website involves beginning on one of the N pages, and then navigating around using the 
links until you decide to stop. That is, while on page i, you may either move to page Li, or stop your browsing 
session.
Assuming you can choose which page you begin the session on, what's the maximum number of different pages 
you can visit in a single session? Note that a page only counts once even if visited multiple times during 
the session.
"""

from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
  return 0


print(getMaxVisitableWebpages(4, [4, 1, 2, 1]))
print(getMaxVisitableWebpages(5, [4, 3, 5, 1, 2]))
print(getMaxVisitableWebpages(10, [3, 5, 3, 1, 2, 4, 5, 6, 7, 8]))
print(getMaxVisitableWebpages(5, [2,4,2,2,3]))