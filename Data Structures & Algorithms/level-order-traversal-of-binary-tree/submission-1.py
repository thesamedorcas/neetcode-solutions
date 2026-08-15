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

        q= deque()
        q.append(root)

        res=[]
        while q:
            l=len(q)
            curl=[]

            for _ in range(l):
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

                curl.append(curr.val)
            res.append(curl)
        return res


        