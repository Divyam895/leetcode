# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ls=[]
        def trav(p,node):
            if not node:
                return
            if not node.left and not node.right:
                ls.append(p)
            if node.left:
                trav(p+"->"+str(node.left.val),node.left)
            if node.right:
                trav(p+"->"+str(node.right.val),node.right)
        trav(str(root.val),root)
        return ls