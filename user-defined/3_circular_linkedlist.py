class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break

    # append at the last
    def append(self, data):
        # if no initial nodes
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head

        else:
            node = Node(data)
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = node
            node.next = self.head

    # append node at the start
    def prepend(self, data):
        node = Node(data)
        cur_node = self.head

        # point the next to initial first node
        node.next = self.head

        # no initial nodes 
        if not self.head:
            node.next = node
        
        # nodes already exists 
        else:
            while cur_node != self.head:
                cur_node = cur_node.next
            cur_node.next = node
        self.head = node

    # split the lists
    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0

        prev = None
        cur_node = self.head

        #first list code
        while cur_node and count < mid:
            count += 1
            prev = cur_node
            cur_node = cur_node.next
        prev.next = self.head

        split_list = CircularLinkedList()
        while cur_node != self.head:
            split_list.append(cur_node.data)
            cur_node = cur_node.next
        split_list.append(cur_node.data)

    
    # Delete the node
    def delete(data):
        pass