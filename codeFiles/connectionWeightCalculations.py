def connectionWeights(nodesList, sourceNode, obstacleList) -> list:
    '''
    input:
    nodesList [[xLoc, yLoc, zLoc], [...]]
    sourceNode [[xLoc, yLoc, zLoc]]
    obstacleList [[TopLeftX,TopLeftY,BottomRightX,BottomRightY,Height], [...]]

    output: 
    list with [[node1, node2, weight], [...], [...]]

    '''
    return 0