class Solution:
    def findTargetSumWays(self, nums):
        index = 0
        curSum = 0
        memo = {}
        return self.helper(nums, S, index, curSum, memo)
    
    def helper(self, nums, target, index, curSum, memo): 
        if (index, curSum) in memo: 
            return memo[(index, curSum)]
        
        if index >= len(nums) and curSum == target: 
            return 1
        if index >= len(nums): 
            return 0
        
        # plusing nums[index] positive
        pos = self.helper(nums, target, index + 1, curSum + nums[index], memo)
        neg = self.helper(nums, target, index + 1, curSum - nums[index], memo)
        
        memo[(index, curSum)] = pos + neg
        
        return memo[(index, curSum)]