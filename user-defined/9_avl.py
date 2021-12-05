class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # perform rotation
        y.left = z
        z.right = T2

        # update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y

    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # perform rotation
        y.right = z
        z.left = T3

        # update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y
    
    
    def insert(self, root, key):
        # 1. perform normal BST
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.height))

        # 3. get the balance factor
        balance = self.getBalance(root)

        # 4. if the node is unbalanced, then try out these 4 cases
        # case 1- left left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        
        # case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.leftRotate(root)

        # case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
    
        return root

    def delete(self, root, key):
        # 1. perform standard BST delete
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

        temp = self.getMinValueNode(root.right)
        root.val = temp.val
        root.right = self.delete(root.right, temp.val)

        # if the tree has only one node, simply return it
        if root is None:
            return root

        # 2. update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Get the balance factor
        balance = self.getBalance(root)

        # 4. if the node is unbalanced, then try out these 4 cases

        # case 1 - LEFT LEFT
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # case 2 - RIGHT RIGHT
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # case 3 - LEFT RIGHT
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
