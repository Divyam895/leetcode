# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum={}
        def trav(level,node):
            if not node:
                return
            if level not in level_sum.keys():
                level_sum[level]=node.val
            else:
                level_sum[level]+=node.val
            trav(level+1,node.left)
            trav(level+1,node.right)
        trav(1,root)
        maxi=0
        sem=-2**31-1
        for i in level_sum.keys():
            if sem<level_sum[i]:
                maxi=i
                sem=level_sum[i]
        return maxi