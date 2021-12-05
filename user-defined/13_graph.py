class Graph:
    def __init__(self, size) -> None:
        self.adJMatrix = []
        self.size = size
        for i in range(size):
            self.adJMatrix.append([0 for i in range(size)])

    def __len__(self):
        return self.size


    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d"%(v1, v2))
        self.adJMatrix[v1][v2] = 1


    def remove_edge(self, v1, v2):
        if self.adJMatrix[v1][v2] == 0:
            print("No edge between  %d and %d"%(v1, v2))
            return
        self.adJMatrix[v1][v2] = 0

    

    def print_matrix(self):
        for row in self.adJMatrix:
            for val in row:
                print('{:4}'.format(val), end='')
            print()

def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.print_matrix()
    g.remove_edge(2, 3)
    g.print_matrix()


if __name__ == '__main__':
    main()