#   https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# below is recursion solution
# more better way to solve this is two pass algo
# where we have two pointers, one is 0 and other at n+1
# there will constant gap btw two pointers i.e. n
# now when second pointer reaches end of list.
# delete the first pointer.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def visit(node, target):
    # return the number of node
    if node.next:
        ret = visit(node.next,target)
        if ret == target:
            # delete the node.next
            next_node = node.next
            node.next = next_node.next
        return ret + 1
    else:
        return 1

class Solution:
    # remove nth node from the end of the list
    # in one pass!! -> obviously recursion.
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next:
            length = visit(head, n)
            if length == n:
                # remove the head
                return head.next if head.next else []
            return head
        else:
            if n == 1:
                return []
            else:
                return head

if __name__ == "__main__":
    solution = Solution()
    solution.removeNthFromEnd()