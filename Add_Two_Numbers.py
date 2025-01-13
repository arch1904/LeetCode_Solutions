# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        m = 0
        while l1 != None:
            x = x + l1.val * (10**m)
            l1 = l1.next
            m += 1
        y = 0
        m = 0
        while l2 != None:
            y = y +l2.val *(10**m)
            l2 = l2.next
            m += 1
        z = x + y
        out = []
        if z == 0:
            return ListNode()
        while z != 0:
            out.append(z%(10))
            z = z // 10
        l3 = ListNode()
        l3_temp = l3
        for i in range(len(out) - 1):
            l3.val = out[i]
            l3.next = ListNode()
            l3 = l3.next
        l3.val = out[len(out) - 1]
        l3.next = None
        return l3_temp



        



        