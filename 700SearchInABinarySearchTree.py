# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            elif val == root.val:
                return root
        return None