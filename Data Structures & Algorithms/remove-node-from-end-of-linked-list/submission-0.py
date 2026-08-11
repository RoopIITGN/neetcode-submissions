# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c2 = head
        i = 0
        while(i <= n and c2):
            c2 = c2.next
            i += 1
        if(not c2 and i == n):
            return head.next

        c1 = head
        while(c2):
            c1 = c1.next
            c2 = c2.next
        
        c1.next = c1.next.next
        return head