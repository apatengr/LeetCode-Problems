'''
19. Remove Nth Node From End of List (Difficulty: Medium)

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #slow pointer and fast pointer
        fast = head
        slow = head
        
        # create a difference of n between slow and fast pointers, and set the fast node to end 
        for i in range(n):
            fast = fast.next
            
        # if deleting the first element
        if fast == None:
            return head.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next 
            
        # if deleting the last element
        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
        
        return head
