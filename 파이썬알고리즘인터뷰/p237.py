# 인덱스 m부터 n까지 역순으로 만들어라. 인덱스 m은 1부터.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_by_index(head, left, right):
        
    if not head or left == right:
        return head
    
    root = start = ListNode(None)
    root.next = head
    
    for _ in range(left-1):
        start = start.next
        
    end = start.next
    
    for _ in range(right-left):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    
    return root.next