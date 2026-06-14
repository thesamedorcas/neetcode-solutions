# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        track= [root]

        while track:
            curr= track.pop()
            curr.left, curr.right= curr.right, curr.left

            if curr.left:
                track.append(curr.left)

            if curr.right:
                track.append(curr.right)

        return root
        