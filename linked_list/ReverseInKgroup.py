from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arr_to_list_node(arr):
    dummy = ListNode(0)
    head = dummy
    for val in arr:
        head.next = ListNode(val)
        head = head.next
    return dummy.next


def to_arr(head):
    arr = []
    node = head
    while node:
        arr.append(node.val)
        node = node.next
    return arr


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k < 2:
            return head
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        count = length // k
        if not count:
            return head
        dummy = ListNode()
        main_dummy = dummy
        dummy.next = head
        current = head.next
        prev = head
        k -= 1
        for _ in range(count):
            for _ in range(k):
                tmp = current.next
                prev.next = current.next
                current.next = dummy.next
                dummy.next = current
                current = tmp
            dummy = prev
            prev = current
            current = current.next
        return main_dummy.next


if __name__ == '__main__':
    head = arr_to_list_node([1, 2, 3, 4, 5])
    res = Solution().reverseKGroup(head, 2)
    arr = to_arr(res)
