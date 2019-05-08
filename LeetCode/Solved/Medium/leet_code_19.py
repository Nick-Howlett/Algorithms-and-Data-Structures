class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        lead = head
        trail = head
        for i in range(n):
            lead = lead.next
        if not lead: return head.next
        while lead.next:
            lead = lead.next
            trail = trail.next
        trail.next = trail.next.next
        return head