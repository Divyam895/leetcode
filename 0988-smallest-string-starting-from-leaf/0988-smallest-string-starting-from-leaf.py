# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        mini=None
        def trav(par,node):
            nonlocal mini
            if not node:
                return
            if not node.right and not node.left:
                par=chr(97+node.val)+par
                if mini is None or par<mini:
                    mini=par
                return
            trav(chr(97+node.val)+par,node.left)
            trav(chr(97+node.val)+par,node.right)
        trav("",root)
        return mini