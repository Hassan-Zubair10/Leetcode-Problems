# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderIterative(self, root) -> List[int]:
        if not root:
            return []

        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    
    def preorderRecursive(self, node) -> List[int]:
        if not node:
            return []
        return [node.val] + self.preorderRecursive(node.left) + self.preorderRecursive(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorderRecursive(root)