# 역순으로 저장된 연결 리스트의 숫자 더하기
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):

    root = head = ListNode()

    sum = 0
    carry = 0

    while l1 or l2:

        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))

add_two_numbers(l1,l2)