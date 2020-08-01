"""
https://leetcode.com/problems/find-duplicate-subtrees/
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        freq = {}
        ans = []
        
        # at every node, get a serialization of the node
        def serialization(node): 
            if not node: 
                return "#"
            curSer = "{}, {}, {}".format(node.val, serialization(node.left), serialization(node.right))
            
            if curSer in freq:
                if freq[curSer] == 1: 
                    ans.append(node)
                freq[curSer] += 1
            else: 
                freq[curSer] = 1
            return curSer
        
        serialization(root)
        return ans
                