class Graph:
    def __init__(self,size=5):
        self.matrix = [[False for x in range(size)] for x in range(size)]
        self.nodes = []

    def __str__(self) -> str:
        out = " "
        for node in self.nodes:
            out += node.data
        for i, x in enumerate(self.matrix):
            out += f"\n{self.nodes[i].data}"
            for y in x:
                if y:
                    out += str(1)
                else:
                    out += str(0)
        return out

    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,src, dest):
        self.matrix[src][dest] = True

    def check_edge(self,src, dest) -> bool:
        return self.matrix[src][dest]

class Node:
    def __init__(self, data):
        self.data = data

graph = Graph(5)

graph.add_node(Node('A'))
graph.add_node(Node('B'))
graph.add_node(Node('C'))
graph.add_node(Node('D'))
graph.add_node(Node('E'))

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(2,2)
graph.add_edge(4,0)
graph.add_edge(4,2)

print(graph)
print(graph.check_edge(0,1))
print(graph.check_edge(2,2))

