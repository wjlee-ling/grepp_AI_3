# practice 8
"""
to-do: dummy node가 있을 때 없을 때 코드 비교, 장단점 정리, 최종 링크드 리스트 정리
.getAt()관련 질문..
changes:
changed into (a) a doubly-linked list with (b) dummy head/tail nodes
"""

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None) #dummy node
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount :
            """
            Q.왜 pos의 최대치가 self.nodeCount까지 가능한지??
             if nodeCount == 8 & pos == 8, getAt(8) 이 가능한지?

            대신, self.nodeCount-1까지면
            if nodeCount == 8 & pos == 7, getAt(7)은 아래에 따라
            """
            return None

        if pos > self.nodeCount //2 :
            # 찾는 position이 중반 이후이면 tail부터 찾는 게 빠름
            # 여전히 O(n)
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos +1:
                # i < 8 - 8  +1 (즉 1)
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        # 앞뒤로 dummy node를 넣음으로써 corner cases를 위한 로직 필요없이
        # 모든 position에 동일한 코드 적용할 수 있음: doubly linked list(w/dummy nodes)의 장점
        prev = self.getAt(pos-1)
        return self.insertAfter(prev, newMode)

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def popAfter(self, target):
        to_pop = target.next
        next = to_pop.next
        next.prev = target
        target.next = next
        self.nodeCount -= 1
        return to_pop.data

    def popAt(self, pos):
        """
        주의사항1: pos(position)의 위치 관련 e.g. 맨 앞이냐, 맨 뒤냐
        2: 현재 리스트의 노드 수가 0이냐, 1이냐, 그 이상이냐
        * doubly linked list w/ dummy nodes로는 코드를 간단하게 통일 가능
        """
        if pos < 0 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos-1)
        return self.popAfter(prev)

    def popBefore(self, target):
        to_pop = target.prev
        prev = to_pop.prev
        prev.next = target
        target.prev = prev
        self.nodeCount -= 1
        return to_pop.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
