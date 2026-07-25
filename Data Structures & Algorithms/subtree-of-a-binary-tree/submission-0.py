# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs1(node,node1):
            if not node:
                return False
            if node.val == node1.val and dfs(node,node1):
                return True
            return dfs1(node.left,node1) or dfs1(node.right,node1)
        
        def dfs(node,node1):
            if not node and not node1:
                return True
            if not node or not node1:
                return False
            if node.val != node1.val:
                return False
            return dfs(node.left,node1.left) and dfs(node.right,node1.right)
        return dfs1(root,subRoot)
        