# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def traverse(root, s_m, target):
            if not root:
                return False
            s_m += root.val
            if s_m == target and not root.left and not root.right:
                return True
            return traverse(root.right, s_m, target) or traverse(root.left, s_m, target)

        if not root:
            return False

        return traverse(root, 0, targetSum)

s = Solution()
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
r = s.hasPathSum(root, targetSum)
print(r)