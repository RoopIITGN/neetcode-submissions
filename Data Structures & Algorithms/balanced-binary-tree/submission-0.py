# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l_h = dfs(node.left)
            r_h = dfs(node.right)
            if(abs(l_h - r_h) > 1):
                raise ValueError("Unbalanced")

            return 1 + max(l_h, r_h)
        
        try:
            dfs(root)
            return True
        except:
            return False
