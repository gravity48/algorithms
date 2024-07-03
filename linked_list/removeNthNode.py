from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        count = 0
        index = 1
        while head:
            count = index
            head = head.next
            index += 1
        prev = dummy
        head = dummy.next
        for _ in range(count - n):
            prev = head
            head = head.next
        prev.next = head.next if head else None
        return dummy.next


class BestSolution:

    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head

