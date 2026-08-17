# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ls={}
        def trav(level,node):
            if not node:
                return
            try:
                if node.val>ls[level]:
                    ls[level]=node.val
            except:
                ls[level]=node.val
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(1,root)
        return list(ls.values())