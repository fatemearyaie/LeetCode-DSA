# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        current = head
        previous = None


        while current:
            if current.val == val:
                if not previous:
                    head = current.next
                    current = head
                else:
                    next_node = current.next
                    previous.next = next_node
                    current = next_node
            else:
                previous = current
                current = current.next

        return head