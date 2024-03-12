# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __diameter(self, root):
        if not root:
            return -1

        left_subtree = self.__diameter(root.left)
        right_subtree = self.__diameter(root.right)

        self.diameter = max(self.diameter, left_subtree + right_subtree + 2)
        return 1 + max(left_subtree, right_subtree)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.__diameter(root)
        return self.diameter