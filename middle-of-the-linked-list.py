# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0 #calc length of list
        p = head
        while (p != None):
            p = p.next
            length = length + 1
        p = head
        c = 0
        while (c < length/2): #find mid val
            p = p.next
            c = c + 1
        return p.val
