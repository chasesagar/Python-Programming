# basic python program for tree traversals

# A class that represents an individual node in a
# Binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder(left, root, right) traversal of binary tree
# using recursion
def printInOrder(node):
    if node:
        printInOrder(node.left)
        print(node.val,end=" ")
        printInOrder(node.right)

# A function to do preorder(root, left,right) traversal of binary tree 
# using recursion
def printPreOrder(node):
    if node:
        print(node.val, end=" ")
        printPreOrder(node.left)
        printPreOrder(node.right)


# A function to do postorder(left,right, root) traversal of binary tree 
# using recursion
def printPostOrder(node):
    if node:
        printPostOrder(node.left)
        printPostOrder(node.right)
        print(node.val, end=" ")
    

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Inorder traversal of binary tree is:", end=" ")
printInOrder(root)
print("\nPreorder traversal of binary tree is:", end=" ")
printPreOrder(root)
print("\nPostorder traversal of binary tree is:", end=" ")
printPostOrder(root)