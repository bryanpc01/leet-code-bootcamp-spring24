# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        # Base Case
        if not root:
            return []

        queue = deque([root])

        while queue:
            num_of_nodes_at_level = len(queue)
            r_ptr = None

            for i in range(num_of_nodes_at_level):
                node = queue.popleft()

                r_ptr = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            output.append(r_ptr)

        return output
