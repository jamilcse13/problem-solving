# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            arr.append(stack[-1].val)
            root = stack.pop().right
        return arr


# Time Complexity: O(n)
# Space Complexity: O(n)