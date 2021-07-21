# Single Linked List
# ref - https://velog.io/@woga1999/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EB%A7%81%ED%81%AC%EB%93%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8
'''
print_all - 모든 노드 값 출력
get_node - 노드 인덱스 알아내기
append - 맨 뒤에 노드 추가
insert - 원하는 위치에 노드 추가
delete - 원하는 위치의 노드 삭제
'''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SList(object):
    def __init__(self,data):
        self.head = Node(data)
        self.size = 0

    def print_all(self):
        cur = self. head

        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, idx):
        cnt = 0
        node = self.head

        while cnt < idx:
            cnt += 1
            node = node.next

        return node

    def append(self, data):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        
        cur.next = Node(data)

    def insert(self, data, idx):
        new_node = Node(data)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        node = self.get_node(idx-1) # insert될 자리의 앞 노드 호출
        next_node = node.next 
        node.next = new_node
        new_node.next = next_node

    def delete(self, idx):
        
        if idx == 0:
            self.head = self.head.next
            return

        node = self.get_node(idx-1)
        node.next = node.next.next

   

