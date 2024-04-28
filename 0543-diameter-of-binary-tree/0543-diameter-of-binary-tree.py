# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def diameter(root):
            if not root:
                return -1
            
            left = diameter(root.left)
            right = diameter(root.right)
            res[0] = max(res[0], 2+left+right)
            return 1 + max(right, left)
        
        diameter(root)
        return res[0]