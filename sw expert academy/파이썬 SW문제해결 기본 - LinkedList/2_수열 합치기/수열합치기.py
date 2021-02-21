import sys
sys.stdin = open("수열합치기_inputs.txt", 'r')

T = int(input())


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList(object):
    def __init__(self):
        new_node = Node('Head')
        self.before = None
        self.current = None
        self.head = new_node
        self.tail = new_node
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        self.length += 1

    def first(self):
        if self.length == 0:
            return None
        self.before = self.head
        self.current = self.head.link
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.link
        if self.current is None:
            return None
        return self.current.data

    def insertlist(self, new_list):
        insert_num = new_list.first()
        num = self.first()

        for _ in range(self.length):
            if num > insert_num:
                self.before.link = new_list.head.link
                new_list.tail.link = self.current
                self.length += new_list.length
                break
            num = self.next()
        else:
            self.tail.link = new_list.head.link
            self.length += new_list.length

    def result(self):
        array = []
        num = self.first()
        for j in range(self.length):
            array.append(num)
            num = self.next()
        return ' '.join(map(str, array[-1:-11:-1]))


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    first_list = LinkedList()
    for i in map(int, input().split()):
        first_list.append(i)

    for i in range(M-1):
        second_list = LinkedList()
        for j in map(int, input().split()):
            second_list.append(j)
        first_list.insertlist(second_list)

    answer = first_list.result()
    print(f'#{test_case} {answer}')
