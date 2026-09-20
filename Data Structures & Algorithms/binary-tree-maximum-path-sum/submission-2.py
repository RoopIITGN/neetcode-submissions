# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxP = float('-inf')

        def calMaxSum(cNode: Optional[TreeNode]) -> int:
            if not cNode:
                return 0

            nonlocal maxP
            lMax = calMaxSum(cNode.left)
            rMax = calMaxSum(cNode.right)
            nodeMax = max(cNode.val, cNode.val + max(lMax, rMax))
            crMax = max(nodeMax, cNode.val + lMax + rMax)

            if crMax > maxP:
                maxP = crMax
            
            return nodeMax
        
        calMaxSum(root)
        return maxP