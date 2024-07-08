from typing import Optional


# Definition for singly-linked list.
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


def list_node_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        dummy = ListNode(-1000, head)
        prev = dummy
        slow = dummy
        fast = head
        while fast:
            if fast.val < x:
                prev = prev.next
                slow = slow.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
                break
        while fast:
            if fast.val < x:
                slow.next = fast.next
                tmp = prev.next
                prev.next = fast
                fast.next = tmp
                fast = slow.next
                continue
            list_node_arr(head)
            fast = fast.next
            slow = slow.next
        return dummy.next


if __name__ == '__main__':
    head = arr_to_list_node([1, 4, 3, 0, 2, 5, 2])
    res = Solution().partition(head, 3)
    list_node_arr(res)
