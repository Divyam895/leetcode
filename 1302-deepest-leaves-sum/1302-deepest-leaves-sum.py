# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ls={}
        def trav(level,node):
            nonlocal ls
            if not node:
                return 
            if level not in ls.keys():
                ls[level]=node.val
            else:
                ls[level]+=node.val
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(1,root)
        return ls[max(ls.keys())]