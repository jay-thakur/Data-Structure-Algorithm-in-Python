class Node():
    def __init__(self, data=None, next=None) -> None:
            self.data = data
            self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # adding element in the begining of the linked list
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # addig element in the middle of the linked list
    def insertAfter(self, prev_node, data):
        if prev_node == None:
            print("The given previous node must be in linked list")
            return

        # create a node & put data
        node = Node(data)
        
        # make next of new node as next of prev_node
        node.next = prev_node.next

        # make next of prev_node as new node
        prev_node.next = node


    # adding element at the end of linked list
    def insertAtEnd(self, data):
        node = Node(data)

        # if the linked list is empty, then make the new node as head
        if self.head is None:
            self.head = data
            return

        # traverse till the last node
        last = self.head
        while(last.next):
            last = last.next

        # change the next of last node
        last.next = node

    # delete a node -  check this seems wrong
    def deleteAtPos(self, pos):
        cur_node = self.head

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None