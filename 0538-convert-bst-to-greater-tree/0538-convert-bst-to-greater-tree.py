# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(indic,node,s=0):
            if not node:    
                return
            tempval=node.val
            if indic==0:
                node.val=s+node.val+treesum(node.right)
            elif indic==1:
                node.val=s-treesum(node.left)
            elif indic==-1:
                node.val=treesum(node.right)+node.val
            trav(0,node.left,node.val)
            trav(1,node.right,node.val-tempval)
        def treesum(node):
            if not node:
                return 0
            return node.val+treesum(node.left)+treesum(node.right)
        trav(-1,root)
        return root