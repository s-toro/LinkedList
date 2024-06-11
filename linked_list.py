import typing

class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def append_at_start(self, data) -> None:
        if self.head is None:
            self.head = data
            self.tail = self.head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_at_idx(self, data, idx) -> None:
        current_idx = 1
        new_node = Node(data)
        current_node = self.head
        while(current_node.next):
            if current_idx == idx:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_idx += 1
            current_node = current_node.next

    def print_list(self) -> None:
        python_list = []
        current_node = self.head
        while (current_node.next):
            python_list.append(current_node.data)
            current_node = current_node.next
        python_list.append(current_node.data)
        print(python_list)
    
    def length(self) -> int:
        if self.head is None:
            print('No elements in linked list') 
            return
        idx = 1
        current_node = self.head
        while (current_node.next):
            idx += 1
            current_node = current_node.next
        return idx
