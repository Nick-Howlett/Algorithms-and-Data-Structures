# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

#could also insert into a min-heap, but it comes out to the same thing, NlogN.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for llist in lists:
            while llist:
                arr.append(llist.val)
                llist = llist.next
        if not arr: return None
        arr.sort()
        ret = ListNode(arr[0])
        current = ret
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return ret