import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.queueSize = 0

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty queue"

        current_node = self.head
        out = str(current_node.data)

        while current_node.next:
            current_node = current_node.next
            out += " " + str(current_node.data)

        return out[:-2]

    # enqueue adds a node to the end of the queue
    def enqueue(self, data):
        # if this node is the first
        self.queueSize += 1
        if self.isEmpty():
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)

    # dequeue removes and returns the first element of a queue
    def dequeue(self):
        if self.head is None:
            return

        out = self.head.data
        self.head = self.head.next
        self.queueSize -= 1
        return out

    def peek(self):
        if self.isEmpty():
            return
        return self.head.data

    def isEmpty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self.queueSize

    def contains(self, compare) -> bool:
        if self.isEmpty():
            return False
        current_node = self.head
        while current_node:
            if current_node.data == compare:
                return True
            current_node = current_node.next
        return False


if __name__ == "__main__":
    quoo = Queue()
    for i in range(100):
        quoo.enqueue(random.randrange(100))

    print(quoo)
    print(f"Size: {quoo.size()}")
    print(quoo.peek())
    print(quoo.dequeue())
    print(f"Size: {quoo.size()}")
    print(quoo)

    print(quoo.contains(77))
