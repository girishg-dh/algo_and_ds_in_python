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
  max_distance_traversed = 0
  max_distance_dict = dict()
  for i in range(N):
    if i in max_distance_dict:
      continue
    distance_traversed = 1
    visited = {i}
    current, next = i, L[i] - 1
    while next not in visited:
      current = next
      distance_traversed += 1
      visited.add(current)
      max_distance_dict[current] = distance_traversed
      next = L[current] - 1
    max_distance_traversed = max(max_distance_traversed, distance_traversed)
  return max_distance_traversed 



print(getMaxVisitableWebpages(4, [4, 1, 2, 1]))
print(getMaxVisitableWebpages(5, [4, 3, 5, 1, 2]))
print(getMaxVisitableWebpages(10, [3, 5, 3, 1, 2, 4, 5, 6, 7, 8]))
print(getMaxVisitableWebpages(5, [2,4,2,2,3]))