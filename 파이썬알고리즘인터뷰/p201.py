# 연결 리스트가 팰린드롬 구조인지 판별

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 혜린
def is_palindrome(head: ListNode) -> bool:

    if not head:
        return True

    vals = []
    node = head

    while node is not None:
        vals.append(node.val)
        node = node.next 

    return vals == vals[::-1]

# 런너 기법 풀이 - △
# 연결리스트를 순회할 때 2개의 포인터를 동시에 사용. (빠른 런너, 느린 런너)
def is_palindrome(head: ListNode) -> bool:

    rev = None
    slow = fast = head

    # 역순 연결 리스트
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev

head = ListNode(1, ListNode(2, None))
is_palindrome(head)
