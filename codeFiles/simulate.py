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
        self.heap = heapq.heapify(graph.connectionWeights(self.nodesList, self.sourceNode, self.obstaclesList))
        print('done')