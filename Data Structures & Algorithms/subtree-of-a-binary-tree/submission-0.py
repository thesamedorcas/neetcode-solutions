# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def sametree(p, q):
            if not p or not q:
                return p==q
            if p.val!=q.val:
                return False

            return sametree(p.left,q.left ) and sametree(p.right, q.right)

        if not root and not subRoot:
            return True

        stack= [root]

        while stack:
            currp= stack.pop()

            

            my_check= sametree(currp, subRoot)

            if my_check==True:
                return True
            else:
                if currp.left:
                    stack.append(currp.left)
                if currp.right:
                    stack.append(currp.right)

        return False
                


        