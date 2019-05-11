# Kept for posterity, cleaner solution at link below.
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lead = trail = head
        if not head: return None
        for _ in range(k - 1):
            lead = lead.next
            if not lead: return head
        temp = lead.next
        lead.next = None
        head, lead = self.reverse_llist(trail)
        lead.next = temp
        trail = head
        while lead:
            prev = lead
            for _ in range(k):
                lead = lead.next
                trail = trail.next
                if not lead: return head
            temp = lead.next
            lead.next = None
            trail, lead = self.reverse_llist(trail)
            lead.next = temp
            prev.next = trail
        return head
        
    def reverse_llist(self, head):
        prev = None
        current = head
        while current:
          current.next, current, prev = prev, current.next, current
        return prev, head