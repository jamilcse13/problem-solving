# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		# Check if tree is mirror of itself
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, root1, root2):
		# If both trees are empty, then they are mirror images
        if root1 is None and root2 is None:
            return True
        
		# For two trees to be mirror images,
		# 	the following three conditions must be true
		# 	1 - Their root node's key must be same
		# 	2 - left subtree of left tree and right subtree
		# 	  of the right tree have to be mirror images
		# 	3 - right subtree of left tree and left subtree
		# 	   of right tree have to be mirror images
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return (self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))
        
		# If none of the above conditions is true then root1
		# and root2 are not mirror images
        return False