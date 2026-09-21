# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def addNode(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                res += ",N"
                return
            res = res + "," + str(node.val)
            addNode(node.left)
            addNode(node.right)
        
        addNode(root)
        # print(f"Serialized = {res}")
        return res    
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        i = 1
        # print(f"val = {vals}")
        def buildNode():
            nonlocal i
            if vals[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = buildNode()
            node.right = buildNode()

            return node
        
        return buildNode()
