'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        l3 = ListNode(0)
        head = l3
        
        # stop when both are None
        while l1 != None or l2 != None: 
            if l1 == None:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            
            elif l2 == None:
                l3.next = ListNode(l1.val)
                l1 = l1.next
        
            else:
                # comparison
                if l1.val < l2.val:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
            l3 = l3.next
            
        # head would return inclusive of 0, which we don't want
        head = head.next
        return head
