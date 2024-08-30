from typing import List


class Node:
    n = int()
    color = int()

    def __init__(self):
        self.edges = list()

    def __str__(self):
        return f'N{self.n}'


nilNode = Node()
nilNode.n = -1


class Edge:
    start = nilNode
    end = nilNode
    weight = float()

    def __str__(self):
        return f'{self.start} -> {self.end} [label="{self.weight}"]'


class Graph:
    nodes: List[Node] = list()
    edges = []

    def loadFromMatrix(self, filename: str):
        f = open(filename)
        N, M = map(int, f.readline().split())
        for n in range(N):
            node = Node()
            node.n = n
            self.nodes.append(node)

        for i in range(N):
            j_ids = f.readline().strip().split('\t')
            for j in range(N):
                if not i == j:
                    a = j_ids[j]
                    if not a == 'inf' and float(a):
                        w = float(a)
                        e = Edge()
                        e.start = self.nodes[i]
                        e.end = self.nodes[j]
                        e.weight = w
                        self.nodes[i].edges.append(e)
                        self.edges.append(e)

    def save_to_dot(self, filename):
        with open(filename, 'wt') as f:
            f.write('digraph Gr { \n')
            for node in self.nodes:
                f.write(str(node) + ';\n')
            for edge in self.edges:
                f.write(str(edge) + ';\n')
            f.write('}\n')


if __name__ == '__main__':
    gr = Graph()
    gr.loadFromMatrix('graph_matrix.txt')
    gr.save_to_dot('output.dot')






