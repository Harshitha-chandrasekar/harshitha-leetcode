# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def subtreehasnode(root,v):
            if not root:
                return False
            if root.val == v.val:
                return True
            return subtreehasnode(root.left,v) or subtreehasnode(root.right,v)

        def check(root):
            if not root:
                return
            if subtreehasnode(root.left,p) and subtreehasnode(root.left,q):
                return check(root.left)
            elif subtreehasnode(root.right,p) and subtreehasnode(root.right,q):
                return check(root.right)
            else:
                return root

        return check(root)
