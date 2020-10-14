from tree_visual import deserialize, TreeNode, drawtree
from typing import List
from queue import Queue

# Umberalla Traverse
# vertical order ->
#   1. left child's right child
#   2. right child's left child


# we need to rank all the nodes
# left = parent - 1
# right = parent + 1


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        root.rank = 0
        minrank, maxrank = self.rank_tree(root)
        anslen = abs(minrank) + abs(maxrank) + 1
        ans = [[] for i in range(anslen)]
        self.traverse(root, ans, abs(minrank))
        return ans

    def traverse(self, root, ans, zeroindex):
        if not root:
            return
        # since we report the value in the order of top to botton
        # use the level order traversal
        queue = Queue()
        queue.put([root])
        while not queue.empty():
            nodes = queue.get()
            # sort the nodes in ascending order
            nodes = sorted(nodes, key=lambda node: node.val)
            next_level_nodes = []
            for node in nodes:
                rank = node.rank
                index = zeroindex + rank
                ans[index].append(node.val)
                next_level_nodes.extend(self.get_children(node))
            if next_level_nodes:
                queue.put(next_level_nodes)

    def get_children(self, root):
        ans = []
        if root.left:
            ans.append(root.left)
        if root.right:
            ans.append(root.right)
        return ans

    def rank_tree(self, root):
        """ ranks all the root's childern """
        parent_rank = root.rank
        max_rank = min_rank = parent_rank
        if root.left:
            root.left.rank = parent_rank - 1
            # rank the left subtree
            left_ranks = self.rank_tree(root.left)
            min_rank = min([left_ranks[0], min_rank])
            max_rank = max([left_ranks[1], max_rank])
        if root.right:
            root.right.rank = parent_rank + 1
            # rank the right subtree
            right_ranks = self.rank_tree(root.right)
            min_rank = min([right_ranks[0], min_rank])
            max_rank = max([right_ranks[1], max_rank])
        return (min_rank, max_rank)


if __name__ == "__main__":
    # tree = deserialize("[3,9,20,5,null,15,7,null,6]")
    # tree = deserialize("[0,2,1,null,4,null,3]")
    # tree = deserialize("[0,1,null,null,2,6,3,null,null,null,4,null,5]")
    # tree = deserialize("[3,9,20,5,null,15,7,null,6]")
    # tree = deserialize("[0,8,1,null,null,3,2,null,4,5,null,null,7,6]")
    tree = deserialize("[0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]")
    ans = Solution().verticalTraversal(tree)
    drawtree(tree)
    print(ans)
