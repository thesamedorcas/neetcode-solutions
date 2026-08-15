# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        '''
        level traversal kepe track of length and return end
        '''

        if not root:
            return []

        q= deque()
        q.append(root)

        res=[]

        while q:
            l= len(q)
            curl=0
            for _ in range(l):
                cur= q.popleft()
                curl=cur

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
            res.append(curl.val)

        return res
        