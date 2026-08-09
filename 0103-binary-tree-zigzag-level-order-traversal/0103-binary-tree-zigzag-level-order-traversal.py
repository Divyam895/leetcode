# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ds={}
        ls=[]
        def trav(level,node):
            if not node:
                return
            if level in ds.keys():
                if level%2!=0:
                    ds[level]=[node.val]+ds[level]
                else:
                    ds[level].append(node.val)
            else:
                ds[level]=[node.val]
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(0,root)
        for i in ds.keys():
            ls.append(ds[i])
        return ls
            