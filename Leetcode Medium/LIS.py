"""
Is this the most typical DP problem or what?
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

def lengthOfLIS(nums): 
    # initialize minimum longest subsequence at nums[i] using dpTable
    dpTable = [1] * len(nums)

    for i in range(1, len(nums)): 
        for j in range(i): 
            if nums[i] > nums[j]: 
                dpTable[i] = max(dpTable[i], dpTable[j]+1)

    return max(dpTable)


