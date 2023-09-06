# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head
        nxt = current.next
        if not nxt:
            return current
        else:
            while nxt:
                newNode = ListNode(math.gcd(current.val, nxt.val))
                current.next = newNode
                newNode.next = nxt
                current = nxt
                nxt = nxt.next
        return head
