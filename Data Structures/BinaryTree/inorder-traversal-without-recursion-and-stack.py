# Inorder(left,root,right) traversal without recursion and without stack.
# Using Morris teaversal, wecan traversal the tre without using stack and recursion.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def morris_traversal(root):
    # 1. Initialize current as root
    current = root

    # until current is not null
    while current is not None:
        if current.left is None:
            yield current.data
            current = current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right
            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                yield current.data
                current = current.right

root = Node(1,right=Node(3),
            left=Node(2,left=Node(4),right=Node(5))
            )
  
for v in morris_traversal(root):
    print(v, end=' ')