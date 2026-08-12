"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head):
            return None
        c_o = head
        
        while(c_o):
            c_c = Node(c_o.val, c_o.next, c_o.random)
            c_o.next = c_c
            c_o = c_c.next

        c_c = head.next
        while(c_c):
            if(c_c.random):
                c_c.random = c_c.random.next
            if(c_c.next):
                c_c = c_c.next.next
            else:
                break
        
        c_c = head.next
        while(c_c.next):
            c_c.next = c_c.next.next
            c_c = c_c.next
        c_c = head.next
        head.next = None
        return c_c
