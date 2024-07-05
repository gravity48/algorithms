from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link_list_from_arr(arr: list):
    dummy = ListNode()
    head = dummy
    for val in arr:
        dummy.next = ListNode(val)
        dummy = dummy.next
    return head.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1000, head)
        slow = dummy
        fast = dummy
        fast2 = dummy.next
        is_dublicate = False
        while fast2.next:
            fast2 = fast2.next
            fast = fast.next
            if fast.val == fast2.val:
                is_dublicate = True
                continue
            else:
                if not is_dublicate:
                    slow.next = fast
                    slow = slow.next
                else:
                    is_dublicate = False
        if not is_dublicate:
            slow.next = fast.next
        else:
            slow.next = None
        return dummy.next


if __name__ == '__main__':
    head = link_list_from_arr([1, 1])
    Solution().deleteDuplicates(head)
