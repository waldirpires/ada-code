# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        return pathSum(root, 0, targetSum)

def pathSum(node, sum, target):
    if not node.left and not node.right:
        return node.val + sum == target

    if not node.right:
        return pathSum(node.left, sum + node.val, target)
    if not node.left:
        return pathSum(node.right, sum + node.val, target)


    return pathSum(node.left, sum + node.val, target) or pathSum(node.right, sum + node.val, target)

s = Solution()
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
r = s.hasPathSum(root, targetSum)
print(r)