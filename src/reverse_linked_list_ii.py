# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        current, counter = head, 1
        if left == 1:
            prev = None
            node_before_left = None
            new_tail = head
        else:
            while counter < left - 1:
                current = current.next
                counter += 1

            node_before_left = current
            new_tail = current.next

            prev = current
            current = current.next
            counter += 1
            
        while counter <= right:
            next = current.next
            current.next = prev
            prev = current
            current = next
            counter += 1
        
        if left != 1:
            new_tail.next = current
            node_before_left.next = prev
        else:
            head.next = current
            return prev

        return head
        