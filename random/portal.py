"""
You've found yourself in a grid of cells with R rows and C columns. The cell in the ith row from the top and jth column from the left contains one of the 
following (indicated by the character Gi,j):

If Gi,j = ".", the cell is empty.
If Gi,j = "S", the cell contains your starting position. There is exactly one such cell.
If Gi,j = "E", the cell contains an exit. There is at least one such cell.
If Gi,j = "#", the cell contains a wall.
Otherwise, if Gi,j is a lowercase letter (between "a" and "z", inclusive), the cell contains a portal marked with that letter.
Your objective is to reach any exit from your starting position as quickly as possible. Each second, you may take either of the following actions:

Walk to a cell adjacent to your current one (directly above, below, to the left, or to the right), 
as long as you remain within the grid and that cell does not contain a wall.
If your current cell contains a portal, teleport to any other cell in the grid containing a portal marked with the same letter as your current cell's portal.
Determine the minimum number of seconds required to reach any exit, if it's possible to do so at all. If it's not possible, return -1 instead.
"""
from typing import List
from collections import deque, defaultdict

# Write any import statements here

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  # Write your code here
  portalDict = defaultdict(list)
  next_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  alphabets = 'abcdefghijklmnopqrstuvwxyzS'
  for i in range(R):
    for j in range(C):
      if G[i][j] in alphabets:
        portalDict[G[i][j]].append((i, j))
  solutions = []
  visited = set()
  queue = deque()
  startR, startC = portalDict['S'][0]
  queue.append((startR, startC, 0))
  # visited.add((startR, startC))
  while queue:
    r, c, time = queue.popleft()
    if (r, c) in visited or G[r][c] == '#':
      continue
    visited.add((r, c))
    if G[r][c] == 'E':
      solutions.append(time)
      continue
    currentValue = G[r][c]
    if currentValue in alphabets:
      for portalR, portalC in portalDict[currentValue]:
        if portalR == r and portalC == c:
          continue
        queue.append((portalR, portalC, time + 1))
    for nextR, nextC in next_positions:
      if 0 <= r + nextR < R and 0 <= c + nextC < C:
        queue.append((r + nextR, c + nextC, time + 1))
  return -1 if len(solutions) == 0 else min(solutions)


print(getSecondsRequired(3, 3, [['.', 'E', '.'], ['.', '#', 'E'], ['.', 'S', '#']]))
print(getSecondsRequired(3, 4, [['a','.','S','a'],['#','#','#','#'],['E','b','.','b']]))
print(getSecondsRequired(3, 4, [['a','.','S','a'],['#','#','#','#'],['E','b','.','a']]))
print(getSecondsRequired(1, 9, [['x','S', '.', '.', 'x', '.', '.', 'E', 'x']]))