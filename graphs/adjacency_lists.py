from linked_list import LinkedList


class Graph:
    def __init__(self) -> None:
        self.alist = []

        """
    def __init__tr__(self) -> str:
        out = ""
        for node in self.alist:
            current_list = node.head
            out += str(current_list.data)
            while current_list.next:
                out += current_list.data
                current_list = current_list.next
            out += "\n"

        return out
    """

    def add_node(self, node):
        self.alist.append(LinkedList().insert_end(node))

    def add_edge(self, src, dst):
        current_list = self.alist[src]

    def check_edge(self, src, dst):
        pass


class Node:
    def __init__(self, data):
        self.data = data


graph = Graph()
graph.add_node(Node("A"))
graph.add_node(Node("B"))
graph.add_node(Node("C"))
graph.add_node(Node("D"))
graph.add_node(Node("E"))

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 0)
graph.add_edge(4, 2)

print(graph)

for node in graph.alist:
    print(node)
