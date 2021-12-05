class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # append a node at the end
    def append(self, data):
        if self.head is None:
            node = Node(data)
            node.prev = None
            self.head = node
        else:
            node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next

            # we have reached the last node, now let's append the node
            cur_node.next = node
            node.prev = cur_node
            node.next = Node

    # append a node at the start
    def prepend(self, data):
        # in case if there is no node in initial DLL
        if self.head is None:
            node = Node(data)
            node.prev = None
            self.head = node
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
            node.prev = Node

    # delete a node
    def delete(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node == key and cur_node == self.head:
                # case 1 - if there is only one node in the list
                if not cur_node.next:
                    cur_node = None
                    self.head = None
                    return

                # case 2 - to delete first node
                else:
                    # making a new pointer next to next node of current node
                    nxt = cur_node.next
                    cur_node.next = None
                    nxt.prev = None
                    cur_node = None
                    self.head = nxt
                    return

            elif cur_node == key:
                # case 3 - to delete middle node
                if cur_node.next:
                    # making a new pointer prev and nxt
                    nxt = cur_node.next
                    prev = cur_node.prev

                    #stretch next pointer to next node
                    prev.next = nxt

                    #stretch next pointer to previous node
                    nxt.prev = prev
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return

                # case 4 - to delete last node
                else:
                    prev = cur_node.prev
                    prev.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
            cur_node = cur_node.next


