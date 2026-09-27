# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float('-inf')

        def getpath(root):
            if not root:
                return 0

            left = max(getpath(root.left),0)
            right = max(getpath(root.right),0)

            curr = left + right + root.val

            self.m = max(self.m,curr)

            return max(left,right) + root.val

        getpath(root)
        return self.m
