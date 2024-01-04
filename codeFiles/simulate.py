import codeFiles as graph
import heapq

class simulate:
    def __init__(self, versionNumber, nodesFile, sourceFile, obstacleFile):
        #load all data here
        self.dataNum = 1
        self.nodesList = graph.nodesLoader(nodesFile)
        self.sourceNode = graph.sourceLoader(sourceFile)
        self.obstaclesList = graph.obstacleLoader(obstacleFile)
        self.nodesList.append(self.sourceNode[0])
        self.heap = []

        #error handling for input data
        self.obstaclesList = graph.obstacleErrorHandling(self.obstaclesList) 
        self.nodesList = graph.nodeHandling(self.nodesList)
        
        self.n = len(self.nodesList) #total number of nodes (include source not no duplicates)

        self.nodesToKeys, self.keysToNodes = graph.mapping(self.nodesList)
        print("Assigning node numbers to keys")
        for key, (x,y,z) in self.keysToNodes.items():
            print(key, ":", (x,y,z))

        print("initial setup done\n\n")

        self.costToConnect = 0
        
    
    #just testing if the class structure works
    def testFile(self):
        return 1
    def getNodesList(self):
        return self.nodesList
    def getSourceNode(self):
        return self.sourceNode
    def getObstaclesList(self):
        return self.obstaclesList

    def connectionWeights(self):
        print('Forming Connection Weights\n\n')
        self.heap = graph.connectionWeights(self.nodesList, self.sourceNode, self.obstaclesList)
        heapq.heapify(self.heap)
        print(heapq.heappop(self.heap))
        print('done\n\n')

    def runAlgorithm(self):
        #declare a disjoint set union find data structure

        self.uf = graph.unionFindStruct(self.n)
        totalIslands = self.n

        while self.heap and totalIslands != 1:
            weight, node1, node2 = heapq.heappop(self.heap)
            #map it to node numbers

            #need tuple since list cannot be keys for dictionary
            nodeNum1 = self.nodesToKeys[tuple(node1)]
            nodeNum2 = self.nodesToKeys[tuple(node2)]

            if (not self.uf.alreadyConnected(nodeNum1, nodeNum2)):
                self.uf.union(nodeNum1, nodeNum2)
                self.costToConnect += weight
                print("source node", nodeNum1, "connects to source node", nodeNum2)
                totalIslands -= 1

        print("total cost:", self.costToConnect)

