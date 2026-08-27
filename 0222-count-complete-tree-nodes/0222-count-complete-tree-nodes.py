# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        def trav(node):
            if not node:
                return 0
            left=node.left
            right=node.right
            lh=0
            rh=0
            while left:
                lh+=1
                left=left.left
            while right:
                rh+=1
                right=right.left
            if lh==rh:
                return 1+((1<<lh)-1)+trav(node.right)
            else:
                return 1+((1<<rh)-1) + trav(node.left)
        return trav(root)
            
        

