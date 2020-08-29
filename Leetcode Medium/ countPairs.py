"""
1530. Number of Good Leaf Nodes Pairs
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        
        def helper(node): 
            nonlocal count
            if node is None: 
                return []
            if node.left is None and node.right is None: 
                return [1]
            
            left = helper(node.left)
            right = helper(node.right)
            
            retArr = []
            
            for i in range(len(left)): 
                for j in range(len(right)):
                    if left[i] + right[j] <= distance:
                        count += 1

            for n in left + right: 
                if n + 1 < distance: 
                    retArr.append(n+1)
            return retArr
            
        
        helper(root)
        return count