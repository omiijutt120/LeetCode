# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        head = ListNode()      # first node of answer
        temp = head            # pointer to build answer
        carry = 0

        while l1 or l2:

            num1 = 0
            num2 = 0

            if l1:
                num1 = l1.val

            if l2:
                num2 = l2.val

            total = num1 + num2 + carry

            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit)
            temp = temp.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            temp.next = ListNode(carry)

        return head.next