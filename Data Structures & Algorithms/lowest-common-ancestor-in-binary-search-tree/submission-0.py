# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(root.val == p.val) or (root.val == q.val):
            return root
        mn = mx = TreeNode()
        if(p.val < q.val):
            mn, mx = p, q
        else:
            mn, mx = q, p
    
        if(mn.val < root.val and mx.val > root.val):
            return root
        
        elif(mn.val < root.val and mx.val < root.val):
            return self.lowestCommonAncestor(root.left, mn, mx)

        else:
            return self.lowestCommonAncestor(root.right, mn, mx)