# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        last = None

        while dummy:
            temp = dummy.next
            dummy.next = last
            last = dummy
            dummy = temp
        
        return last