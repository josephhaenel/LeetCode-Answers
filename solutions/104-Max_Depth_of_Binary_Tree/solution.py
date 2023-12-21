# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Time Complexity: O(N)
Space Complexity: O(log(N)) In average case when tree is balanced.
    Worst Case: O(N)

LeetCode Difficulty: Easy
'''
class Solution:
    def maxDepth(self, root) -> int:
        stack = list()
        depth = 0

        if root is not None:
            stack.append( (1, root) ) # (depth, node)

        while stack:
            curDepth, root = stack.pop()
            
            if root is not None:
                depth = max(depth, curDepth)
                stack.append((curDepth + 1, root.left))
                stack.append((curDepth + 1, root.right))
        
        return depth
        