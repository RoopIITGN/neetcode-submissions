# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = defaultdict(list)
        if not root:
            return []

        queue = deque([root])
        res = []

        while(queue):
            ln = len(queue)
            nodes_i = []
            for i in range(ln):
                ele = queue.popleft()
                nodes_i.append(ele.val)

                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            
            res.append(nodes_i)

        return res