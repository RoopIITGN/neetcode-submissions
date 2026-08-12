# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(not l1 and not l2):
            return None
        elif(not l1):
            return l2
        elif(not l2):
            return l1

        c = 0
        head = prev = None
        while(l1 and l2):
            s = l1.val + l2.val + c
            c = s//10
            v = s%10
            nw = ListNode(v, None)
            if prev:
                prev.next = nw
            else:
                head = nw
            prev = nw
            l1, l2 = l1.next, l2.next
        
        while(l1):
            s = l1.val + c
            c = s//10
            v = s%10
            nw = ListNode(v, None)
            prev.next = nw
            prev = nw
            l1 = l1.next

        while(l2):
            s = l2.val + c
            c = s//10
            v = s%10
            nw = ListNode(v, None)
            prev.next = nw
            prev = nw
            l2 = l2.next
        
        if(c > 0):
            nw = ListNode(c, None)
            prev.next = nw
        
        return head
        
