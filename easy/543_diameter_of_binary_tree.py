# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def height(node):
    if not node:
        return -1

    return 1 + max(height(node.left), height(node.right))

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # max of the following
        # diameter of left SBT
        # diameter of right SBT
        # path going through root ==> heigh of LSBT + height of RSBT + 1

        if not root:
            return 0 # there is no node, the length of path is 0

        lheight = height(root.left)
        rheight = height(root.right)

        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)

        return max(max(ldiameter, rdiameter), (lheight + rheight + 2))

if __name__ == "__main__":
    solution = Solution()
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    assert solution.diameterOfBinaryTree(node) == 3