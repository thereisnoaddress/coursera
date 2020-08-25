class Solution:
    def maxProduct(self, nums) -> int:
    
        
        # must keep track of two things: curMax and curMin
        curMax, curMin, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)): 
            tempMax = max(nums[i], nums[i]*curMax, nums[i]*curMin)
            tempMin = min(nums[i], nums[i]*curMin, nums[i]*curMax)
            curMax, curMin = tempMax, tempMin
            ans = max(curMax, ans)
        
        return ans
        