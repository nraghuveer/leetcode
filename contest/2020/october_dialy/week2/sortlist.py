# Given the head of a linked list, return the list after sorting it in ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


# lets use the merge sort with the linked lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        nh = self._sort(head)
        arr = []
        while nh:
            arr.append(nh.val)
            nh = nh.next
        return arr

    def middle(self, head):
        if not head or not head.next:
            return None
        # we are sure that there are atleast two nodes...
        slow_prev = None
        slow = fast = head
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        slow_prev.next = None
        return slow

    def _sort(self, head):
        if not head:
            return None
        middle = self.middle(head)
        if not middle:
            return head
        left = self._sort(head)
        right = self._sort(middle)
        return self._merge(left, right)

    def _merge(self, left, right):
        dummy = head = ListNode(0)
        while left and right:
            if left.val <= right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        # either one is exhausted or both are exhaust
        if bool(left) != bool(right):
            if right:
                head.next = right
            else:
                head.next = left
        return dummy.next


def build_ll(arr):
    cur = head = ListNode(arr[0])
    for i in arr[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


if __name__ == "__main__":
    s = Solution()
    assert s.sortList(build_ll([3, 2, 1, 5, 4])) == [1, 2, 3, 4, 5]
