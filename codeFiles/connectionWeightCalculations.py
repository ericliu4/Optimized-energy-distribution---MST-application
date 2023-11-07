def connectionWeights(nodesList, sourceNode, obstacleList) -> list:
    n = len(nodesList)
    '''
    input:
    nodesList [[xLoc, yLoc, zLoc], [...]]
    sourceNode [[xLoc, yLoc, zLoc]]
    obstacleList [[TopLeftX,TopLeftY,BottomRightX,BottomRightY,Zstart, Height], [...]]

    output: 
    list with [[node1, node2, weight], [...], [...]]

    '''

    ###2 parts
    #1. add the extra weight due to obstacle


    #2. add distance and just height difference b/w them
    return [[0,2,3,4]]