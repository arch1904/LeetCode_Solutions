'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        new_h = ListNode(head.val)
        new_iter = new_h
        old_iter = head
        while old_iter != None:
            if old_iter.val == new_iter.val:
                old_iter = old_iter.next
            else:
                new_iter.next = ListNode(old_iter.val)
                new_iter = new_iter.next
                old_iter = old_iter.next
        return new_h