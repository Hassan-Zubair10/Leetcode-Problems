# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None

        while fast != None and fast.next != None:
            if slow == fast:
                return True
            slow, fast = slow.next, fast.next.next
        
        return False