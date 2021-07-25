# 페어의 노드 스왑

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 혜린
def swap_node(head):

    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head

input = ListNode(1,ListNode(2,ListNode(3, ListNode(4))))
swap_node(input)

