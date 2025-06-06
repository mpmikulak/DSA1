class Stack:
    def __init__(self) -> None:
        self.body = []
        self.size = 0

    def __str__(self) -> str:
        out = ""
        for v in self.body:
            out += str(v) + "->"
        return out[:-2] + "\n"

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def peek(self):
        # Sanitary check to see if we are peeking at an empty Stack
        if self.isEmpty():
            return None

        return self.body[self.size - 1]

    def push(self, value):
        self.body.append(value)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        value = self.body.pop()
        self.size -= 1
        return value


if __name__ == "__main__":
    stack = Stack()

    for i in range(1, 11):
        stack.push(i)

    print(stack)
