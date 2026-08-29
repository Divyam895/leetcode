# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        return ([(sum(levells[i])/len(levells[i])) for i in levells.keys()])