"""
Leetcode 322

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # using a DP table to keep track of minimum number of coins needed for amount DP[i]
        # bottom-up approach: start with 0 and work my way up to amount
        DP = [amount + 1] * (amount + 1)
        
        DP[0] = 0
        
        for i in range(1, amount + 1): 
            for coin in coins: 
                if i - coin >= 0: 
                    DP[i] = min(DP[i - coin] + 1, DP[i])
                    
        return -1 if DP[-1] == (amount+1) else DP[-1]
            