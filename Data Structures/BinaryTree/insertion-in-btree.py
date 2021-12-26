# Python program to insert elements in binary tree

class newNode:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

""" Inorder traversal of a binary tree  """
def Inorder(temp):
    if(not temp):
        return
    Inorder(temp.left)
    print(temp.key, end=" ")
    Inorder(temp.right)

""" Function to insert element in binary tree """
def insert(temp,key):
    if(temp == None):
        root = newNode(key)
        return
    q = []
    q.append(temp)
    # Do level order trasversal until we find an empty place
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (temp.left == None):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if (temp.right == None):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

#driver

if __name__ == "__main__":
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)

    print("Inorder traversal before insertion:", end=" ")
    Inorder(root)

    key = 12
    insert(root,key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    Inorder(root)