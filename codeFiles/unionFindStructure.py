class unionFindStruct:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def alreadyConnected(self, node1, node2):
        return self.root[node1] == self.root[node2]
    
    def find(self, node1):
        if self.root[node1] != node1:
            self.root[node1] = self.find(self.root[node1])
        return self.root[node1]
    
    
    def union(self, node1, node2):
        rootNode1 = self.find(node1)
        rootNode2 = self.find(node2)

        if rootNode1 == rootNode2:
            return
        if self.rank[rootNode1] > self.rank[rootNode2]:
            self.root[rootNode2] = rootNode1
        elif self.rank[node2] > self.rank[rootNode1]:
            self.root[rootNode1] = rootNode2
        else:
            self.root[rootNode1] = rootNode2
            self.rank[rootNode2] += 1
        return

    #standard union find structure that has 4 functions
    #rank is used to shorten computation time