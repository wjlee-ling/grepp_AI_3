# practice 8
"""
to-do: dummy node가 있을 때 없을 때 코드 비교, 장단점 정리, 최종 링크드 리스트 정리
test add
"""

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        """
        주의사항1: pos(position)의 위치 관련 e.g. 맨 앞이냐, 맨 뒤냐
        2: 현재 리스트의 노드 수가 0이냐, 1이냐, 그 이상이냐
        """
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if self.nodeCount == 1:
            curr = self.head
            self.head = None
            self.tail = None
            self.nodeCount -= 1
            return curr.data

        if pos == 1:
            curr = self.head
            self.head = curr.next
            self.nodeCount -=1
            return curr.data

        elif pos == self.nodeCount:
            prev = self.getAt(pos-1)
            prev.next = None
            curr = self.tail
            self.tail = prev
            self.nodeCount -=1
            return curr.data
        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next
            self.nodeCount -=1
            return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
