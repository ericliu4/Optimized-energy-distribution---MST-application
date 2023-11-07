import codeFiles as graph


import sys
print(sys.executable)


algorithmVersion = 1
inputDataFile = '../inputDataFiles/inputDataNodes - Sheet1.csv'
inputSourceFile = '../inputDataFiles/sourceNodes - Sheet1.csv'
inputObstacleFile = '../inputDataFiles/obstacleData - Sheet1.csv'
instance1 = graph.simulate(algorithmVersion, inputDataFile, inputSourceFile, inputObstacleFile)
print(instance1.testFile())

