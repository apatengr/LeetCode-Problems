'''2. Add Two Numbers (Medium)

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        value = l1.val + l2.val + carry
        carry = value // 10
        value = value % 10
        newNode = ListNode(value) # storing the result into new linked list
        
        if l1.next != None or l2.next != None or carry != 0: # either of linked list's next node has to be not none or carry has to be 0 to not call the recursive function 
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            newNode.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return newNode
