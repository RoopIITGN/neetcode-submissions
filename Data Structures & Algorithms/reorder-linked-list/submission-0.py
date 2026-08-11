# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        c1 = c2 = head
        # while(c2.next):
        while(c2):
            if(c2.next):
                c1 = c1.next
                c2 = c2.next.next  
            else:
                break

        cur = c1.next
        c1.next = None
        prev = None
        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        c1 = head
        c2 = prev

        while(c2):
            n1 = c1.next
            n2 = c2.next
            c1.next = c2
            c2.next = n1
            c1 = n1
            c2 = n2

        return None




