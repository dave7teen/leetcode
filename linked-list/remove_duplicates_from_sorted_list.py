'''
Given a sorted linked list, delete all duplicates such that each element
appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        list_node = head
        while list_node and list_node.next:
            if list_node.val == list_node.next.val:
                list_node.next = list_node.next.next
            else:
                list_node = list_node.next
        return head
