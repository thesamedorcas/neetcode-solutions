# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        bfs
        level
        parents keep track of max and chekc if greater
        
        '''

        if not root:
            return 0

        q= deque()
        q.append((root, root.val))
        res=1
        while q:
            curr, maxv= q.popleft()
            if curr.left:
                if maxv<= curr.left.val:
                    res+=1
                q.append((curr.left,max(maxv, curr.left.val) ))
            if curr.right:
                if maxv<= curr.right.val:
                    res+=1
                q.append((curr.right,max(maxv, curr.right.val) ))

        return res

            
        
        