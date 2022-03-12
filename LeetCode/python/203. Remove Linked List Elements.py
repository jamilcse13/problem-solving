# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        
        if temp is None:
            return temp
        
        while temp is not None and temp.val == val:
            head = head.next
            temp = head
        
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        
        return head