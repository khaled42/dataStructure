class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def put(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
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
