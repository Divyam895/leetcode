# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        depth={root.val:0}
        parent={root.val:-1}
        q=deque([root])
        while q:
            l=len(q)
            for i in range(l):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                    parent[n.left.val]=n.val
                    depth[n.left.val]=depth[n.val]+1
                if n.right:
                    q.append(n.right)
                    parent[n.right.val]=n.val
                    depth[n.right.val]=depth[n.val]+1
        return depth[x]==depth[y] and parent[x]!=parent[y]