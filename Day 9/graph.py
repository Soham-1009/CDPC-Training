import sys


class Graphs:

    def __init__(self):

        self.nodes = []
        self.graph = []
        self.nodeCount = 0

    def addnode(self, v):

        if v in self.nodes:
            print(v, "is already present")

        else:
            self.nodeCount += 1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp = []
            for x in range(self.nodeCount):
                temp.append(0)
            self.graph.append(temp)
            print(v, "is added")

    def addEdge_Undirected_Unweighted(self, v1, v2):

        if v1 not in self.nodes:
            print(v1, "not present")
            return
        if v2 not in self.nodes:
            print(v2, "not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = 1
        self.graph[index2][index1] = 1
        print("Edge Added")

    def addEdge_Undirected_Weighted(self, v1, v2, w):
        if v1 not in self.nodes:
            print(v1, "not present")
            return
        if v2 not in self.nodes:
            print(v2, "not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = w
        self.graph[index2][index1] = w

        print("Weighted Edge Added")

    def addEdge_Directed_Weighted(self, v1, v2, w):
        if v1 not in self.nodes:
            print(v1, "not present")
            return

        if v2 not in self.nodes:
            print(v2, "not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = w
        print("Directed Weighted Edge Added")

    def addEdge_Directed_Unweighted(self, v1, v2):
        if v1 not in self.nodes:
            print(v1, "not present")
            return
        if v2 not in self.nodes:
            print(v2, "not present")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = 1
        print("Directed Unweighted Edge Added")

    def printGraph(self):
        print(" ", *self.nodes)
        for i in range(self.nodeCount):
            print(self.nodes[i], end=" ")
            for j in range(self.nodeCount):
                print(self.graph[i][j], end=" ")
            print()

    def deleteGraph(self,v):
        if v not in self.nodes:
            print(v,"not present")
        else:
            nodeCount-=1
            index1=self.nodes.index(v)
            self.nodes.pop(index1)
            self.graph.pop(index1)
            for x in self.graph:
                x.pop(index1)
            print(v,"is deleted")
if __name__ == "__main__":

    obj = Graphs()

    while True:

        print("\n1. Add a single node using adjacency matrix representation")
        print("2. Add edge undirected unweighted")
        print("3. Add edge undirected weighted")
        print("4. Add edge directed weighted")
        print("5. Add edge directed unweighted")
        print("6. Print Graph")
        print("7. Delete Graph")
        print("0. Exit\n")

        n = int(input("Enter the choice: "))

        if n == 1:

            v = input("Enter the vertex: ")
            obj.addnode(v)

        elif n == 2:

            v1 = input("Enter Vertex 1: ")
            v2 = input("Enter Vertex 2: ")
            obj.addEdge_Undirected_Unweighted(v1, v2)

        elif n == 3:
            v1 = input("Enter Vertex 1: ")
            v2 = input("Enter Vertex 2: ")
            w = input("Enter the weight: ")
            obj.addEdge_Undirected_Weighted(v1, v2, w)

        elif n == 4:
            v1 = input("Enter Vertex 1: ")
            v2 = input("Enter Vertex 2: ")
            w = input("Enter the weight:")
            obj.addEdge_Directed_Weighted(v1, v2, w)

        elif n == 5:
            v1 = input("Enter Vertex 1: ")
            v2 = input("Enter Vertex 2: ")
            obj.addEdge_Directed_Unweighted(v1, v2)

        elif n == 6:

            obj.printGraph()

        elif n == 7:

            obj.deleteGraph(v)

        elif n == 0:

            sys.exit(0)
