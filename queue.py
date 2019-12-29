from node import LinkedListNode as Node

class Queue:
    def __init__(self):
        self.head = None
        self.queue = None

    def put(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.queue = node
        else:
            self.queue.next = node
            self.queue = node

    def pop(self):
        if self.head is None:
            return None
        x = self.head.data
        self.head = self.head.next
        return x

    def empty(self):
        if self.head is None:
            return False
        else:
            return True

    def print_queue(self):
        temp = self.head

        while temp != None:
            print(temp.data, ' -> ', end=' ')
            temp = temp.next
        print()

    def size(self):
        temp = self.head
        cpt = 0
        while temp != None:
            cpt += 1
            temp = temp.next
        return cpt
