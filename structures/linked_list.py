class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        if self.head is None:
            return "Empty list"
        current_node = self.head
        out = str(current_node.data)
        while current_node.next:
            current_node = current_node.next
            out += str(current_node.data)
        return out

    def is_empty(self):
        return self.head is None

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)
        self.size += 1

    def remove_end(self):
        if self.is_empty():
            return
        i = 1
        current_node = self.head
        while i < self.size:
            print(i)
            current_node = current_node.next
            i += 1
        current_node.next = None
        self.size -= 1

    def update_node(self, index, value):
        if self.is_empty() or index > self.size:
            return

        i = 0
        current_node = self.head
        while i < index:
            current_node = current_node.next
            i += 1
        current_node.data = value

    def contains(self, data) -> bool:
        if self.is_empty():
            return False

        current_node = self.head
        while current_node.next:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
