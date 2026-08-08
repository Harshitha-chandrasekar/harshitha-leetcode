"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dicti = {}

        def dfs(node):
            if not node:
                return None

            if node in dicti:
                return dicti[node]

            copy = Node(node.val)
            dicti[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)
