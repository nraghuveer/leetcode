# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# TODO: check how to for the format given in  description

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self,root):
        """Serializes the subtree

        :param root: root of the subtree
        :type root: TreeNode
        """
        if not root:
            return None

        return {
            "val": root.val,
            "left" : self.serialize(root.left) if root.left else None,
            "right" : self.serialize(root.right) if root.right else None
        }

    def deserialize(self,data):
        """Deserialize the subtree. recursion friendly

        :param root: root of the subtree
        :type root: TreeNode
        """
        if data == None: return None

        root = TreeNode(data['val'])
        root.left = self.deserialize(data['left'])
        root.right = self.deserialize(data['right'])

        return root

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    data = Codec().serialize(root)
    print(data)
    root = Codec().deserialize(data)
    print(Codec().serialize(root))

    print('done')