from collections import deque
from typing import List


class Solution:

  def remainingMethods(
      self, n: int, k: int, invocations: List[List[int]]
  ) -> List[int]:
    
    edges = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in invocations:
      edges[u].append(v)
      indegree[v] += 1

    # 2. Perform BFS from buggy method k to identify suspicious methods
    queue = deque([k])
    suspicious = [0] * n
    suspicious[k] = 1

    while queue:
      curr = queue.popleft()
      for v in edges[curr]:
        indegree[v] -= 1
        if not suspicious[v]:
          suspicious[v] = 1
          queue.append(v)

    can_remove = True
    for i in range(n):
      if suspicious[i] and indegree[i] > 0:
        can_remove = False
        break

    
    if can_remove:
      return [i for i in range(n) if not suspicious[i]]
    return list(range(n))