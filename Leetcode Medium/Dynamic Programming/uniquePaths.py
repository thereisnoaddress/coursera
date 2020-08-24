"""
Leetcodd 62. https://leetcode.com/problems/unique-paths/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # idea: use DP matrix to store # of ways to get to END at every step
        # DP[i][j] = DP[i+1][j] + DP[i][j+1] 
        
        # init
        DP = [[-1] * n for _ in range(m)]
        
        # all DP[m][#] and all DP[#][n] set to m and n
        # since you can only go down and right
        for i in range(n): 
            DP[m- 1][i] = 1
        for i in range(m): 
            DP[i][n - 1] = 1
        
        # start from m-1 to 0
        for i in range(m-1, 0, -1): 
            for j in range(n-1, 0, -1):
                if DP[i-1][j-1] == -1: 
                    DP[i-1][j-1] = DP[i][j-1] + DP[i-1][j]
        
        return DP[0][0]