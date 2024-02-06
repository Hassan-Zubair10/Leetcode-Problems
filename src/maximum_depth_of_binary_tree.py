# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_subtree = self.maxDepth(root.left) + 1
        right_subtree = self.maxDepth(root.right) + 1

        return max(left_subtree, right_subtree)
