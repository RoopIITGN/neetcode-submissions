# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while(q):
            rNode = None
            ln = len(q)

            for i in range(ln):
                node = q.popleft()
                if node:
                    rNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rNode:
                    res.append(rNode.val)
        return res
