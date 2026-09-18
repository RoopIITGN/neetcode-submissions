# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex = 0

        inorderMap = {val : idx for idx, val in enumerate(inorder)}

        def buildNode(left: int, right: int) -> Optional[Treenode]:
            nonlocal preorderIndex
            if(left > right):
                return
            
            rootVal = preorder[preorderIndex]
            root = TreeNode(rootVal)
            preorderIndex += 1

            mid = inorderMap[rootVal]
            root.left = buildNode(left, mid-1)
            root.right = buildNode(mid+1, right)

            return root
        
        return buildNode(0, len(preorder) - 1)