import codeFiles as graph

class simulate:
    def __init__(self, versionNumber, nodesFile, sourceFile, obstacleFile):
        #load all data here
        self.dataNum = 1
        self.nodesList = graph.nodesLoader(nodesFile)
        self.sourceNode = graph.sourceLoader(sourceFile)
        self.obstaclesList = graph.obstacleLoader(obstacleFile)
    
    #just testing if the class structure works
    def testFile(self):
        return 1