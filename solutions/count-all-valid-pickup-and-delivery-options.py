class Solution:
  def countOrders(self, n: int) -> int:
    # This is kinda self evident, it's just DP
    # I wanna say that there should be a math based solution that is O(1)
    # But I dunno

    mod = 10 ** 9 + 7
    
    # 500 * 500 possible states
    @cache
    def dp(P, D):
      if P == 1 and D == 0: return 1
      if P == 0 and D == 1: return 1
      
      count = 0

      # Check if we can deliver
      if D > 0: count += D * dp(P, D - 1)
      
      # Check if we can pickup
      if P > 0: count += P * dp(P - 1, D + 1)

      return count % mod
    
    return dp(n, 0)
