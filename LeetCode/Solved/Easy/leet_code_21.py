class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        ret = None
        if l1.val < l2.val:
            ret = l1
            l1 = l1.next
        else:
            ret = l2
            l2 = l2.next
        current = ret
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l2 if l2 else l1
        return ret