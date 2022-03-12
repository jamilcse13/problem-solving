# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}
        temp = head
        
        while temp is not None:
            if temp.val in hashMap:
                prev.next = temp.next
                temp = temp.next
            else:
                hashMap[temp.val] = 1
                prev = temp
                temp = temp.next
        return head