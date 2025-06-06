class Dynamic_Array:
    def __init__(self, capacity=10):
        self.size = 0
        self.capacity = capacity
        self.body = [None] * capacity

    def __str__(self) -> str:
        if self.size == 0:
            return "Empty Array"
        out = "["
        for i in range(0, self.capacity):
            out += str(self.body[i]) + ", "
        return out[:-2] + "]"

    def add(self, data):
        if self.size >= self.capacity:
            print("growing")
            self.grow()
        self.body[self.size] = data
        self.size += 1

    def grow(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.body[i]
        self.body = new_array
        self.capacity = new_capacity

    def shrink(self):
        new_capacity = self.capacity // 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.body[i]
        self.body = new_array
        self.capacity = new_capacity

    def insert(self, index, data):
        if self.size >= self.capacity:
            self.grow()
        for i in range(self.size, index, -1):
            self.body[i] = self.body[i - 1]
        self.body[index] = data
        self.size += 1

    def delete(self, data):
        for i in range(self.size):
            if self.body[i] == data:
                for j in range(i, self.size):
                    self.body[j] = self.body[j + 1]
                self.body[i] = None
                self.capacity -= 1
            if self.size <= self.capacity // 3:
                self.shrink()
            break

    def search(self, data) -> int:
        for i in range(self.size):
            if self.body[i] == data:
                return i
        return -1


if __name__ == "__main__":
    da = Dynamic_Array()
    for i in range(50):
        da.add(i)
    print(da)

    da.insert(3, 77)
    print(da)

    da.delete(77)
    print(da)

    print(da.search(3))
