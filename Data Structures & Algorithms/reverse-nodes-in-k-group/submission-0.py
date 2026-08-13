# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d = ListNode(-1, head)
        g_prev = d
        while(True):
            k_nd = self.getKth(g_prev, k)
            if not k_nd:
                break
            g_next = k_nd.next

            prev, cur = g_next, g_prev.next
            while(cur != g_next):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = g_prev.next
            g_prev.next = k_nd
            g_prev = tmp

        return d.next

    def getKth(self, cur: ListNode, k: int) -> Optional[ListNode]:
        kth = ListNode()
        while(cur and k>0):
            cur = cur.next
            k -= 1
        return cur