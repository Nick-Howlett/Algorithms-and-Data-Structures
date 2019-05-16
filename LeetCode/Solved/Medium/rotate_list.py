class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
          return head
        lead = trail = head
        length = 0
        while lead:
          lead = lead.next
          length += 1
        k = k % length
        if k == 0:
          return head
        lead = head
        for i in range(k):
          lead = lead.next
        while lead.next:
          lead = lead.next
          trail = trail.next
        temp = trail.next
        trail.next = None
        lead.next = head
        head = temp
        return head