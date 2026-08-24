# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum=0
        def trav(indic,node):
            nonlocal sum
            if not node:
                return
            if indic==1 and not node.left and not node.right:
                sum+=node.val
            trav(1,node.left)
            trav(0,node.right)
        trav(0,root)
        return sum