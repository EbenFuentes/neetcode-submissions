# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # do dfs, returns [True/False, height]
        def dfs(root):
            # base case: empty node, handle return
            if not root:
                return [True, 0]
            # dfs on left/right subtree
            left, right = dfs(root.left), dfs(root.right)
            # balanced node is left/right = balanced, and height <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # return [True/False, height of current node]
            return [balanced, 1 + max(left[1], right[1])]
        # run dfs on root node and return T/F value (index 0)
        return dfs(root)[0]
