import codeFiles as graph

import sys
print(sys.executable)


algorithmVersion = 1
inputDataFile = 'inputDataFiles/InputDataNodes - Sheet1.csv'
inputSourceFile = 'inputDataFiles/sourceNodes - Sheet1.csv'
inputObstacleFile = 'inputDataFiles/obstacleData - Sheet1.csv'
instance1 = graph.simulate(algorithmVersion, inputDataFile, inputSourceFile, inputObstacleFile)
#print(instance1.testFile())
print(instance1.getNodesList())
print(instance1.getSourceNode())
print(instance1.getObstaclesList())

print('\n\ninput data loaded\n\n')


#add weights using a riemann sum technique (for most accurate cost)
instance1.connectionWeights()
print('simulation complete')

