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
            addedNumber=0
            if l1 is not None:
                addedNumber+=l1.val
                l1=l1.next
            if l2 is not None:
                addedNumber+=l2.val
                l2=l2.next
            addedNumber+=carry
            curNode.val=addedNumber%10
            carry=addedNumber//10
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
