from tree_visual import deserialize, TreeNode, drawtree


class Solution:
    def traverse(self, root, x, y, level):
        if not root:
            return False, level
        if root.left and (root.left.val == x or root.left.val == y):
            return True, level
        if root.right and (root.right.val == x or root.right.val == y):
            return True, level
        return False, level

    def _areCousins(self, root, x, y, level):
        left_ret = self._areCousins(root.left, x, y, level+1)
        right_ret = self._areCousins(root.right, x, y, level+1)
        return left_ret[0] ^ right_ret[0], level+1

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # traverse the  left and right get the result
        return self._areCousins(root, x, y, 0)[0]

if __name__ == "__main__":
    # tree = deserialize('[1,3,2,null,null,7,4,null,null,5,6,null,8,null,9]')
    tree = deserialize('[1,2,4,3,19,10,5,15,8,null,null,13,14,null,6,null,17,null,null,null,null,18,null,7,11,null,null,null,null,null,9,16,12,null,null,20]')
    drawtree(tree)
    solution = Solution().isCousins(tree, 11,17)
    print(solution)
