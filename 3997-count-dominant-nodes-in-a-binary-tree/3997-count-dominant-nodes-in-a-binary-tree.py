# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count=0
        def trav(node):
            nonlocal count
            if not node:
                return float('-inf')
            left=trav(node.left)
            right=trav(node.right)
            subtree=max(node.val,left,right)
            if node.val==subtree:
                count+=1
            return subtree
        trav(root)
        return count

