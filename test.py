from stack import Stack
from queue import Queue

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
