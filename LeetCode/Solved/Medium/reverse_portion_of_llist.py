class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start = ListNode(False)
        start.next = head
        trail, lead = start, head
        for _ in range(n - 1):
            lead = lead.next
        for _ in range(m - 1):
            trail = trail.next
        curr = trail.next
        prev = lead.next
        end = prev
        trail.next = lead
        while curr != end:
             curr.next, prev, curr = prev, curr, curr.next
        return start.next