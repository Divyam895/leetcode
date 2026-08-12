# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi=0
        level=0
        def trav(level,node):
            nonlocal maxi
            if not node:
                return
            if level>maxi:
                maxi=level
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(1,root)
        return maxi