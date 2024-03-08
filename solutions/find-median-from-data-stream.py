# We can solve this problem by using heaps
# Consider `m` to be the median
# A min-heap to store all elements greater than `m`
# A max-heap to store all elements lesser than `m`
# Whenever the balance of the is off by more than 1, rebalance

import heapq as hq

class MedianFinder:
  def __init__(self):
    self.m = None
    self.right = [] # This is a min-heap
    self.left = [] # This is a max-heap

  def addNum(self, num: int) -> None:
    if self.m == None:
      self.m = num
      return
    
    if num >= self.m: hq.heappush(self.right, num)
    else: hq.heappush(self.left, -num)
    
    # Attempt a rebalance
    self.balance()

  def balance(self):
    diff = len(self.right) - len(self.left)

    # Check if a balance is required
    if diff >= 0 and diff < 2: return # No need to rebalance

    while len(self.right) - 1 > len(self.left):
      hq.heappush(self.left, -self.m)
      self.m = hq.heappop(self.right)
    
    while len(self.left) > len(self.right):
      hq.heappush(self.right, self.m)
      self.m = -hq.heappop(self.left)

  def findMedian(self) -> float:
    l_sz = len(self.left)
    r_sz = len(self.right)
    if (l_sz + r_sz + 1) % 2 == 0: return (self.m + self.right[0]) / 2
    return self.m


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
