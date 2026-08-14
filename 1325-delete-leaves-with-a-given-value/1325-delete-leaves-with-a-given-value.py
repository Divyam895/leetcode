# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def trav(node):
            if not node:
                return False
            if not node.right and not node.left and node.val==target:
                return True
            if trav(node.left):
                node.left=None
                return trav(node)
            if trav(node.right):
                node.right=None
                return trav(node)
        if trav(root):
            root=None
        return root