# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        current_queue, next_queue = [root], []
        result, level = [[]], 0

        while current_queue:
            node = current_queue.pop(0)
            result[level].append(node.val)

            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

            if not current_queue:
                current_queue = next_queue
                next_queue = []
                level += 1
                if current_queue:
                    result.append([])

        return result
            
