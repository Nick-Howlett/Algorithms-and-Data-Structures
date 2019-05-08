class Solution:
    def change(self, amount: int, coins: List[int], memo = {}) -> int:
        key = f"{amount}: {coins}"
        if amount == 0:
            return 1
        if key in memo:
          return memo[key];
        if len(coins) == 0:
          return 0
        total = 0
        qty = 0
        while qty * coins[-1] <= amount:
          total += self.change(amount - qty * coins[-1], coins[:-1], memo)
          qty += 1
        memo[key] = total
        return total