# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(part,par,node):
            if not node:
                return False
            if node.val==0:
                if subdfs(node.left) and subdfs(node.right):
                    if part==1:
                        par.left=None
                    elif part==2:
                        par.right=None
            trav(1,node,node.left)
            trav(2,node,node.right)
        def subdfs(node):
            if not node:
                return True
            if node.val==1:
                return False
            return subdfs(node.right) and subdfs(node.left)
        if subdfs(root):
            return None 
        trav(-1,None,root)
        return root