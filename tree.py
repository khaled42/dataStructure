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


    def print_inorder(self):
        pass

    def print_preorder(self):
        pass

    def print_postorder(self):
        pass

# =========== test ============
arry = [1, 2, 3, 4, 5, 6, 7]
bt = BinaryTree()
for e in arry:
    bt.add(e)

print(bt.root.right.right.data)
