from typing import List
from collections import Counter
import copy

class Solution:
  def minTransfers(self, transactions: List[List[int]]) -> int:
    counts = Counter()
    for [_from, _to, _amt] in transactions:
      counts[_from] -= _amt
      counts[_to] += _amt

      if counts[_from] == 0: counts.pop(_from)
      if counts[_to] == 0: counts.pop(_to)
    
    values = list(map(lambda k: k[1], counts.most_common()))
    counts = Counter(values)

    visited = set()
    def backtrack(counts, score = 0, total = 0):
      if total == 0: 
        return score

      print(counts, score, total)
      min_score = float('inf')

      for k1 in counts:
        for k2 in counts:
          if (k1, counts[k1], k2, counts[k2], total, score) in visited: continue
          visited.add((k1, counts[k1], k2, counts[k2], total, score))
          visited.add((k2, counts[k2], k1, counts[k1], total, score))
          
          if k1 == k2 and counts[k1] < 2: continue
          elif counts[k1] < 1 or counts[k2] < 1: continue
          
          count_copy = copy.deepcopy(counts)
          
          count_copy[k1] -=  1
          if count_copy[k1] == 0: count_copy.pop(k1)

          count_copy[k2] -=  1
          if count_copy[k2] == 0: count_copy.pop(k2)

          offset = -2
          if k1 + k2 != 0: 
            count_copy[k1 + k2] += 1
            offset += 1

          min_score = min(min_score, backtrack(count_copy, score + 1, total + offset))

      return min_score
    return backtrack(counts, 0, len(values))
