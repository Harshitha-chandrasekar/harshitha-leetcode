# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def find(root):
            if not root:
                return 0

            lefth = find(root.left)
            righth = find(root.right)
            self.diam = max(self.diam,lefth+righth)
            return 1+ max(lefth,righth)

        find(root)
        return self.diam
