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
        self.heap = graph.connectionWeights(self.nodesList, self.sourceNode, self.obstaclesList)
        heapq.heapify(self.heap)
        print(heapq.heappop(self.heap))
        print('done')

    #def runAlgorithm(self):
        #while self.heap:
            #heapq.heappop()
