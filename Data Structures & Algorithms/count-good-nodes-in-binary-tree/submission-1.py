# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        res = 0
        # append root, maxValSeen
        q.append([root, float('-inf')])

        while q:
            qLen = len(q)
            node, maxValSeen = q.popleft()
            if node.val >= maxValSeen:
                res += 1
            
            if node.right:
                q.append([node.right, max(maxValSeen, node.val)])

            if node.left:
                q.append([node.left, max(maxValSeen, node.val)])
        
        return res

        