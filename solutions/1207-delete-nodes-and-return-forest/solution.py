# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        ans = []
        def dfs(root):
            if not root:
                return None

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)

                if root.right:
                    ans.append(root.right)

                return None

            return root

        root = dfs(root)

        if root:
            ans.append(root)

        return ans
