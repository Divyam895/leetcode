# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(node,ls):
            print(ls)
            if not ls:
                return
            if len(ls)==1:
                node.val=ls[0]
                return node
            mx=ls.index(max(ls))
            node.val=ls[mx]
            if ls[0:mx]:
                node.left=TreeNode()
                build(node.left,ls[0:mx])
            try:
                if ls[mx+1:]:
                    node.right=TreeNode()
                    build(node.right,ls[mx+1:])
            except:
                return
        root=TreeNode()
        build(root,nums)
        return root