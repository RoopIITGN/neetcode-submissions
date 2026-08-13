# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return None
        
        if(root.left or root.right):
            right = self.invertTree(root.left) if root.left else None
            left = self.invertTree(root.right) if root.right else None
            root.right = right
            root.left = left

        return root