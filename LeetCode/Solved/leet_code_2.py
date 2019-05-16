class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = None
        current = None
        carry = 0
        while l1 or l2:
          total = 0
          if l1:
            total += l1.val
            l1 = l1.next
          if l2:
            total += l2.val
            l2 = l2.next
          will_carry = False
          total += carry
          if total >= 10:
            will_carry = True
            total -= 10
          if current:
            current.next = ListNode(total)
            current = current.next
          else:
            ret = ListNode(total)
            current = ret
          carry = 1 if will_carry else 0
        if carry:
          current.next = ListNode(carry)
        return ret
        