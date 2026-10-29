# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        
        if not root:
            return res

        while q:
            rightSide = None
            size = len(q)

            for i in range(size):
                node = q.popleft()
                rightSide = node

                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)
        
        return res