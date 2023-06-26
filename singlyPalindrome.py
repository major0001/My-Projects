# Definition of a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Base case: an empty list or list with only one node is a palindrome
        if not head or not head.next:
            return True

        # Find the middle of the linked list using the two-pointer technique
        slow = head        
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list 
        second_half = self.reverse(slow.next)

        # Compare the first half with the reversed second half
        curr1 = head
        curr2 = second_half

        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False

            curr1 = curr1.next
            curr2 = curr2.next

        return True

    def reverse(self, head: ListNode)  -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# example 
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
result = sol.isPalindrome(head)

head1 = ListNode(1)
head1.next = ListNode(2)
result2 = sol.isPalindrome(head1)

print(result)
print(result2)
