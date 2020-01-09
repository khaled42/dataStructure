from node import TreeNode
from queue import Queue
from stack import Stack
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
        else:
            q = Queue()
            q.put(self.root)
            while not q.empty():
                a = q.pop()

                if a.left is None:
                    a.left = node
                    break
                else:
                    q.put(a.left)
                if a.right is None:
                    a.right = node
                    break
                else:
                    q.put(a.right)


def print_inorder_rec(t):
    if t is None:
        return
    print_inorder_rec(t.left)
    print(t.data, end='')
    print_inorder_rec(t.right)

def print_preorder_rec(t):
    if t is None:
        return
    print(t.data, end='')
    print_preorder_rec(t.left)
    print_preorder_rec(t.right)

def print_postorder_rec(t):
    if t is None:
        return

    print_postorder_rec(t.left)
    print_postorder_rec(t.right)
    print(t.data, end='')


# =========== test ============
arry = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
bt = BinaryTree()
for e in arry:
    bt.add(e)
print_inorder_rec(bt.root)
print_preorder_rec(bt.root)
print_postorder_rec(bt.root)
