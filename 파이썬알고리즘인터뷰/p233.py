# 연결 리스트를 홀수번째 노드 다음에 짝수번째 노드가 오도록 재구성하라 (인덱스 X, 번째 O)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 마지막 홀수 노드를 첫번째 짝수 노드와 이어주기
# 

def odd_even_list(head):

    if head is None:
            return None

    odd = head
    even = head.next
    even_head = head.next
    
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
        
    odd.next = even_head
        
    return head

