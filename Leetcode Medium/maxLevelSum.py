"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        levelSumDict = {}
        
        def helper(root, level): 
            if not root.left and not root.right: 
                return
            else: 
                curVals = (root.left.val if root.left else 0) + (root.right.val if root.right else 0)
                if (level + 1) in levelSumDict: 
                    levelSumDict[level+1] += curVals
                else: 
                    levelSumDict[level+1] = curVals
                
                if root.left:
                    helper(root.left, level + 1)
                
                if root.right:
                    helper(root.right, level + 1)
        
        helper(root, 1)
        
        maxSum = -1
        maxLevel = -1 
        
        for level in levelSumDict: 
            if levelSumDict[level] > maxSum: 
                maxSum = levelSumDict[level]
                maxLevel = level
        
        return maxLevel