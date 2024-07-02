from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _init_linked_list(arr: List) -> ListNode:
    head = ListNode()
    _head = head
    for val in arr:
        head.next = ListNode(val)
        head = head.next
    return _head.next


def _arr_permutation(arr, left, right):
    current = left
    for _ in range(right - left):
        elem = arr.pop(current + 1)
        arr.insert(left, elem)
        current += 1
    return arr


def _print_linked_list(head: ListNode, arr):
    if not head:
        return
    arr.append(head.val)
    _print_linked_list(head.next, arr)


class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int):
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next


if __name__ == '__main__':
    head = _init_linked_list([1, 2, 3, 4, 5])
    Solution().reverseBetween(head, 2, 4)
    res = _arr_permutation([1, 2, 3, 4, 5], 1, 3)
