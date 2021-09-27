# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer=ListNode()
        addedNumber,carry=0,0
        continueAddition=True
        curNode=answer
        while(continueAddition):
            if l1 is not None:
                digit1=l1.val
            else: digit1=0
            if l2 is not None:
                digit2=l2.val
            else: digit2=0
            addedNumber=carry+digit1+digit2
            curNode.val=addedNumber%10
            carry=int(addedNumber/10)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            if l1 or l2:
                curNode.next=ListNode()
                curNode=curNode.next
            else: continueAddition=False
        if carry is not 0:
            curNode.next=ListNode()
            curNode=curNode.next
            curNode.val=carry
            curNode.next=None
        else:
            curNode.next=None
        
        return answer
