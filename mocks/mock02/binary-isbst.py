# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, min, max):
            if node == None:
                return True
            if min >= node.val or node.val >= max:
                return False
            return validate(node.left, min, node.val) and validate (node.right, node.val, max)

        return validate(root, float('-inf'), float('inf'))

s = Solution()
