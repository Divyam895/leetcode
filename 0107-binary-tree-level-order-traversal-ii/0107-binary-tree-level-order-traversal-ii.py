# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levells={}
        def trav(level,node):
            if not node:
                return
            try:
                levells[level].append(node.val)
            except:
                levells[level]=[node.val]
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(0,root)
        ls=[levells[x] for x in levells.keys()]
        return ls[::-1]