# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using two loops
        count = 0
        tempT = prev = temp = head
        
        while tempT is not None:
            tempT = tempT.next
            count += 1

        target = count - n + 1
        
        if target == 1:
            head = head.next
            return head
            
        while True:
            target -= 1
            if target == 0:
                break
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
            
        return head