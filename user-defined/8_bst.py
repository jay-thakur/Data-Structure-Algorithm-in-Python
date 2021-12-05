class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

def search(node, key):
    if node is None:
        return node

    if key == node.key:
        return node

    if key > node.key:
        return search(node.right, key)

    if key < node.key:
        return search(node.left, key)


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current


def deleteNode(root, key):
    # Return if tree is empty
    if root is None:
        return root

    # find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif(key > root.key):
        root.right  = deleteNode(root.right, key)

    else:
        # if the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if the node has two children, place the inorder sucessor in position of the node to be deleted
        temp = minValueNode(root.right)
        root.key = temp.key

        # delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
    return root


root = None
root = insert(root, 12)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 100)

s = search(root, 100)
print(s)

root = deleteNode(root, 100)

    