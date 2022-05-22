# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)
    
    def invert(self, root):
        if root is None: 
            return
        else: 
            temp = root  

            # recursive calls
            self.invert(root.left)  
            self.invert(root.right)  

            # swap the pointers in this node
            temp = root.left  
            root.left = root.right  
            root.right = temp
        return root


# Time Complexity: n
# Space Complexity: 1