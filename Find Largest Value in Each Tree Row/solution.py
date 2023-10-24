# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_max(self, arr):
        Max = arr[0].val
        for i in range(1, len(arr)):
            Max = max(Max, arr[i].val)
        return Max

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # bfs
        arr = []
        arr.append(root)
        ans = []

        while arr:
            ans.append(self.get_max(arr))
            next_arr = []
            for node in arr:
                if node.left:
                    next_arr.append(node.left)
                if node.right:
                    next_arr.append(node.right)
            arr = next_arr
        
        return ans
