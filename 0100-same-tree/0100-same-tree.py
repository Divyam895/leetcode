# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(nodep,nodeq):
            if not nodep and not nodeq:
                return True
            if not nodep or not nodeq:
                return False
            if nodep.val!=nodeq.val:
                return False
            return trav(nodep.left,nodeq.left) and trav(nodep.right,nodeq.right)
        return trav(p,q)