# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        levells={}
        def trav(level,node):
            if not node:
                return
            if not node.right and not node.left:
                levells[level]=node.val
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(1,root)
        if not root:
            return 0
        return min(levells)
