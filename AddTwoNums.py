# Definition fo singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode() # create a dummy node as the head of the resulting linked list
        current = dummy # create a current pointer to traverse the linked list
        carry = 0 # initialize the carry to 0

        while l1 or l2 or carry:
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            carry = sum_val // 10 # calculate carry

            digit = sum_val % 10 # calculate the current digit

            current.next = ListNode(digit) # create a new node with the digit
            current =  current.next # move the current pointer to the next node

        return dummy.next # Return the next node of the dummy node - actual head of the resulting linked list


