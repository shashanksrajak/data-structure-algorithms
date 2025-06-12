# Source: https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=blind75
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Topic: LinkedList
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        curr = head
        x = size - n + 1

        for i in range(0, x-2):
            curr = curr.next

        if x > 1:
            curr.next = curr.next.next
        else:
            head = head.next
        return head
