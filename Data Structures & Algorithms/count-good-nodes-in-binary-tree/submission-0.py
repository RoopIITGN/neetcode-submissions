# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        global res 
        res = 1

        def dfs(cur: TreeNode, maxC: int):
            global res
            if(cur.val >= maxC):
                res += 1
                maxC = cur.val
            if cur.left:
                dfs(cur.left, maxC)
            if cur.right:
                dfs(cur.right, maxC)
        
        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)

        return res
        