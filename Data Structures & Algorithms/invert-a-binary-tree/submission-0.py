# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # handle no root case
        if not root:
            return None
        # init deque with root tree
        queue = deque([root])
        # while queue has nodes
        while queue:
            # remove the first node
            node = queue.popleft()
            # swap the left and right children of node
            node.left, node.right = node.right, node.left
            # append left child of the the node to the queue if it has one
            if node.left:
                queue.append(node.left)
            # append the right child of the node to the queue if it has one
            if node.right:
                queue.append(node.right)
            
        return root
        