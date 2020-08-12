"""
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # basic idea: for a given i, you want to find x and y st x + y = -i
        # doing this by using pointers :: DO 2SUM LATER
        
        nums.sort()
        results = []
        
        for i in range(len(nums)): 
            target = -1 * nums[i]
            
            beg, end = i + 1, len(nums) - 1
            
            while beg < end: 
                if nums[beg] + nums[end] == target: 
                    results.append((nums[beg], nums[end], nums[i]))
                    beg += 1
                    end -= 1
                elif nums[beg] + nums[end] < target: 
                    beg += 1
                elif nums[beg] + nums[end] > target: 
                    end -= 1
                    
                
        return set(results)