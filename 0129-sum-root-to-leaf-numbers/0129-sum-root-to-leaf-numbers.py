# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum=0
        def trav(p,node):
            nonlocal sum
            if not node.right and not node.left:
                sum+=int(p)
            if node.left:
                trav(p+str(node.left.val),node.left)
            if node.right:
                trav(p+str(node.right.val),node.right)
        trav(str(root.val),root)
        return sum