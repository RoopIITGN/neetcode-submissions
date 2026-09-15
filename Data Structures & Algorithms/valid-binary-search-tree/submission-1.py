# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isValidNode(node, min_l, max_l):
            if not node:
                return True
            if not (min_l < node.val < max_l):
                return False

            return isValidNode(node.left, min_l, node.val) and isValidNode(node.right, node.val, max_l)

        return isValidNode(root, float('-inf'), float('inf'))