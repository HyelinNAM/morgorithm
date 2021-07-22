# 정렬되어 있는 두 연결 리스트를 합치기

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 혜린
def merge_lists(l1,l2):

    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1 # // l1의 첫번째 val이 l2의 첫번째 val보다 무조건 작거나 같음

    result = l1

    while (not l1) and (not l2):
        if l1.val <= l2.val:
            result.next = l1
            l1 = l1.next

        else:
            result.next = l2
            l2 = l2.next

    # 둘 중 하나가 None이 됨
    if not l1:
        result.next = l1

    else:
        result.next = l2

    return result

# 재귀
def merge_lists(l1,l2):

    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = merge_lists(l1.next, l2)

    return l1


l1 = ListNode(1,ListNode(2,ListNode(4)))
l2 = ListNode(1,ListNode(3,ListNode(4)))

merge_lists(l1,l2)
