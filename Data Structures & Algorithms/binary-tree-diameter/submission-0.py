# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0

            r = dfs(node.right)
            l = dfs(node.left)

            diameter = max(diameter, r + l)

            return 1 + (max(r, l))

        dfs(root)

        return diameter
