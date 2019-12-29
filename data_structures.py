class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def put(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None
        x = self.head.data
        self.head = self.head.next
        return x

    def print_stack(self):
        temp = self.head
        while temp != None:
            print(temp.data, ' -> ', end="")
            temp = temp.next
        print()

    def size(self):
        cpt = 0
        temp = self.head
        while temp != None:
            cpt += 1
            temp = temp.next
        return cpt

# ============== Queue ==============

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

# ================ test ===============
if __name__ == "__main__":
    arry = [1, 2, 3, 4]

    stack = Stack()
    queue = Queue()

    for e in arry:
        stack.put(e)
        queue.put(e)
    print('stack : ', end=" ")
    stack.print_stack()
    print('queue : ', end=" ")
    queue.print_queue()

    print('===============================')
    print('pop methode (stack) : ', stack.pop())
    print('pop methode (queue) : ', queue.pop())
    print('===============================')
    print('stack : ', end=" ")
    stack.print_stack()
    print('queue : ', end=" ")
    queue.print_queue()
