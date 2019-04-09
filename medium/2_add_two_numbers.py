# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def get_reverse_value(l: ListNode):
    if not l.next:
        return str(l.val)

    return get_reverse_value(l.next) + str(l.val)

def attach(host, l):
    """attaches given node at the end of the linked list"""
    if host.next:
        return attach(host.next, l)
    else:
        host.next = l
        return l


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_val = int(get_reverse_value(l1))
        l2_val = int(get_reverse_value(l2))

        return self.reverse_list_node(l1_val + l2_val)

    def reverse_list_node(self, value):
        """returns the value in the reverse linked list"""
        result = None

        if value == 0:
            return ListNode(0)

        while value:
            l = ListNode((value%10))
            if result:
                attach(result, l)
            else:
                result = l

            value = value // 10

        return result


if __name__ == "__main__":
    l1 = ListNode(2)
    l11 = attach(l1, ListNode(4))
    attach(l11, ListNode(3))

    l2 = ListNode(5)
    l22 = attach(l2, ListNode(6))
    attach(l22, ListNode(4))

    result = Solution().addTwoNumbers(ListNode(0),ListNode(0))
    print(get_reverse_value(result))
