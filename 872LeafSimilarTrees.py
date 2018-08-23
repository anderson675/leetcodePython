# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root,rec):
            if not root.left and not root.right:
                rec.append(root.val)
            if root.left:
                dfs(root.left,rec)
            if root.right:
                dfs(root.right,rec)
        rec1, rec2 = [], []
        dfs(root1, rec1)
        dfs(root2, rec2)
        return rec1 == rec2
