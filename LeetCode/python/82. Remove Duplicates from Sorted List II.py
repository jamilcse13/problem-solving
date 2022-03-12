# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}
        run = temp = head
        count = 0
        
        while run is not None:
            if run.val in hashMap:
                hashMap[run.val] += 1
                run = run.next
            else:
                hashMap[run.val] = 1
                run = run.next
               
        while temp is not None:
            if temp.val in hashMap and hashMap[temp.val] > 1:
                if count > 0:
                    prev.next = temp.next
                    temp = temp.next
                else:
                    head = head.next
                    temp = head
            else:
                count += 1
                prev = temp
                temp = temp.next
        
        return head