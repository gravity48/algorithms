from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        arr = []
        dummy = ListNode(-1000)
        dummy.next = head
        while head:
            arr.append(head)
            head = head.next
        k = k % len(arr)
        for _ in range(k):
            prev = arr[-2]
            prev.next = None
            _head = arr[0]
            item = arr.pop(-1)
            dummy.next = item
            item.next = _head
            arr.insert(0, item)
        return dummy.next


class BestSolution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        k = length - (k % length)
        while k > 0:
            cur = cur.next
            k -= 1
        newhead = cur.next
        cur.next = None
        return newhead
