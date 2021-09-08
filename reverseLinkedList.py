# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        elif head.next is None: return head
        else:
            #making first node as the last node of the reversed list
            lastNode=ListNode(head.val,None)
            head=head.next
            #iterating the rest of the linked list
            while(head.next is not None):
                reversedNode=ListNode(head.val,lastNode)
                lastNode=reversedNode
                head=head.next
            #making last node as the first node of the reversed list
            reversedNode=ListNode(head.val,lastNode)
            return reversedNode
