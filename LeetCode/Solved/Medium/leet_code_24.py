# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):         
    self.val = x        
    self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        current = head
        temp = current.next
        current.next = temp.next
        temp.next = current
        head = temp
        while current.next and current.next.next:
            first_node = current.next
            second_node = current.next.next
            current.next = second_node
            temp = second_node.next
            second_node.next = first_node
            first_node.next = temp
            current = first_node
        return head