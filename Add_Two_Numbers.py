'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.


'''
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



        



        