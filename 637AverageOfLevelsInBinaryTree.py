# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        final =[]
        q =[]
        q.append(root)
        while(q):

            length = len(q)
            sum1 =0
            for i in range(length):
                elemne =q.pop(0)
                sum1+=elemne.val
                if elemne.left:
                    q.append(elemne.left)
                if elemne.right:
                    q.append(elemne.right)

            final.append(sum1/length)

        return final