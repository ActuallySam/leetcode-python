# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        current = [root]
        while current:
            level_max = float('-inf')
            next_level = []
            for node in current:
                level_max = max(level_max, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(level_max)
            current = next_level
        
        return res