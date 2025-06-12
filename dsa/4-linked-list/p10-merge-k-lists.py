# Source: https://neetcode.io/problems/merge-k-sorted-linked-lists?list=blind75
# https://leetcode.com/problems/merge-k-sorted-lists/submissions/1655603411/
# Difficulty: Hard
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            head = last = ListNode()

            while list1 and list2:
                if list1.val <= list2.val:
                    last.next = list1
                    last = list1
                    list1 = list1.next
                else:
                    last.next = list2
                    last = list2
                    list2 = list2.next

            last.next = list1 or list2
            return head.next

        dummy_head = None

        for i in range(len(lists)):
            dummy_head = merge(dummy_head, lists[i])

        return dummy_head
