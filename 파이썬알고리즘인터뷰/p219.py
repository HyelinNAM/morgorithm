# 연결 리스트를 뒤집어라

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):

    node, prev = head, None # prev - 이전

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n4.next = n5
n3.next = n4
n2.next = n3
n1.next = n2

reverse_linked_list(n1)