import codeFiles as graph

import sys
print(sys.executable)


algorithmVersion = 1
inputDataFile = 'C:/Users/eric7/OneDrive/Desktop/energyDistributionProject/Optimized-energy-distribution---MST-application/inputDataFiles/InputDataNodes - Sheet1.csv'
inputSourceFile = 'C:/Users/eric7/OneDrive/Desktop/energyDistributionProject/Optimized-energy-distribution---MST-application/inputDataFiles/sourceNodes - Sheet1.csv'
inputObstacleFile = 'C:/Users/eric7/OneDrive/Desktop/energyDistributionProject/Optimized-energy-distribution---MST-application/inputDataFiles/obstacleData - Sheet1.csv'
instance1 = graph.simulate(algorithmVersion, inputDataFile, inputSourceFile, inputObstacleFile)
#print(instance1.testFile())

print(instance1.getNodesList())

print(instance1.getSourceNode())

print(instance1.getObstaclesList())

print('\n\ninput data loaded\n\n')


#add weights using a riemann sum technique (for most accurate cost)
instance1.connectionWeights()

#implements the disjoint set union algorithm
#returns a minimum cost
instance1.runAlgorithm()
print('simulation complete')

print('Found best mapping')

#PRINT DATA STARTING FROM HERE

