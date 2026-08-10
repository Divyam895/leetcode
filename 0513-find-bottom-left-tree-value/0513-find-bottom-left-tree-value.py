# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        value=[-1,2**31-1]
        def trav(level,node):
            nonlocal value
            if not node:
                return
            if level>value[0]:
                value=[level,node.val]
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(0,root)
        return value[1]