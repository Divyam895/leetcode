# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sumls={}
        def trav(node):
            if not node:
                return
            sum=node.val+dfs(node.left)+dfs(node.right)
            try:
                sumls[sum]+=1
            except:
                sumls[sum]=1
            trav(node.left)
            trav(node.right)
        def dfs(node):
            if not node:
                return 0
            return node.val+dfs(node.left)+dfs(node.right)
        trav(root)
        maxfreq=0
        maxi=[]
        for i in sumls.keys():
            if maxfreq<sumls[i]:
                maxi=[i]
                maxfreq=sumls[i]
            elif maxfreq==sumls[i]:
                maxi.append(i)
        return maxi
            