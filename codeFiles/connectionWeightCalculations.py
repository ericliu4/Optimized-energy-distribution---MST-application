import numpy as np

def twoDweightFinder(node1, node2, obstacle1, obstacle2, height):
    # format each input as [x, y]
    NodeLeft = min(node1[0], node2[0])
    NodeRight = max(node1[0], node2[0])
    NodeTop = max(node1[1], node2[1])
    NodeBottom = min(node1[1], node2[1])
    # Obstacle will be top left bottom right sorted, but just in case...
    #Function already made in inputErrorHandling
    ObsLeft = min(obstacle1[0], obstacle2[0])
    ObsRight = max(obstacle1[0], obstacle2[0])
    ObsTop = max(obstacle1[1], obstacle2[1])
    ObsBottom = min(obstacle1[1], obstacle2[1])

    condA = NodeLeft >= ObsRight
    condB = NodeRight <= ObsLeft
    condC = NodeTop <= ObsBottom
    condD = NodeBottom >= ObsTop
    return (not condA and not condB and not condC and not condD)

def DirectionDistMinimizer(dest, source, unitdirection):
    diff = [dest[0]-source[0], dest[1] - source[1], dest[2]-source[2]]
    return abs(np.dot(diff, unitdirection))

def weightFinder(node1, node2, TopLeftX, TopLeftY, BottomRightX, BottomRightY, Zstart, height):
    # format each input as [x, y, z]
    # (x,y,z) = (x1, y1, z1) + t(x2-x1, y2-y1, z2-z1)
    # node1 = source, node2 = dest!!!
    x1, x2, y1, y2, z1, z2 = node1[0], node2[0], node1[1], node2[1], node1[2], node2[2]
    dist = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
    n = [(x2-x1)/dist, (y2-y1)/dist, (z2-z1)/dist] # unit directional vector

    # recall your inputs
    corners = [[TopLeftX, TopLeftY], [TopLeftX, BottomRightY], [BottomRightX, BottomRightY], [BottomRightX, TopLeftY]]
    # corresponds to topleft, bottomleft, bottomright, topright

    vertices = []
    for corner in corners:
        e1 = corner.copy()
        e1.append(Zstart)
        vertices.append(e1)

        e2 = corner.copy()
        e2.append(Zstart+height)
        vertices.append(e2)

    #print(vertices)

    # generate min dist vertex
    minvertex, mindist = None, np.inf
    for v in vertices:
        if DirectionDistMinimizer(v, [x1, y1, z1], n) < mindist:
            mindist = DirectionDistMinimizer(v, [x1, y1, z1], n)
            minvertex = v

    # get adjacent vertices - v in vertices that have only 1 element != minvertex
    for v in vertices:
        # z diff
        if v[0] == minvertex[0] and v[1] == minvertex[1] and v[2] != minvertex[2]:
            v3 = [v[0] - minvertex[0], v[1] - minvertex[1], v[2] - minvertex[2]]
        # y diff
        if v[0] == minvertex[0] and v[1] != minvertex[1] and v[2] == minvertex[2]:
            v2 = [v[0] - minvertex[0], v[1] - minvertex[1], v[2] - minvertex[2]]
        # x diff
        if v[0] != minvertex[0] and v[1] == minvertex[1] and v[2] == minvertex[2]:
            v1 = [v[0] - minvertex[0], v[1] - minvertex[1], v[2] - minvertex[2]]
    w = [x1 - minvertex[0], y1 - minvertex[1], z1 - minvertex[2]]

    w1 = np.dot(w, v1)
    w2 = np.dot(w, v2)
    w3 = np.dot(w, v3)
    n1 = np.dot(n, v1)
    n2 = np.dot(n, v2)
    n3 = np.dot(n, v3)

    cond1 = (n1 != 0 and abs(w2-(w1*n2/n1)) <= 1 and abs(w3-(w1*n3/n1)) <= 1)
    cond2 = (n2 != 0 and abs(w1 - (w2 * n1 / n2)) <= 1 and abs(w3 - (w2 * n3 / n2)) <= 1)
    cond3 = (n3 != 0 and abs(w1 - (w3 * n1 / n3)) <= 1 and abs(w2 - (w3 * n2 / n3)) <= 1)

    # add extra weight
    if (cond1 or cond2 or cond3): return height*2 + dist # bonus # actually implement min dist of any axis cuz height is z axis only
    else: return dist


def connectionWeights(nodesList, sourceNode, obstacleList) -> list:
    n = len(nodesList)
    '''
    input:
    nodesList [[xLoc, yLoc, zLoc], [...]]
    sourceNode [[xLoc, yLoc, zLoc]]
    obstacleList [[TopLeftX,TopLeftY,BottomRightX,BottomRightY,Zstart, Height], [...]]

    output:  
    list with [weight, node1, node2], [...], [...]] # I THINK THIS IS THE NEW FORMAT??
    '''
    master_list = []
    for index, node1 in enumerate(nodesList):
        for node2 in nodesList[index+1:]:
            x1, x2, y1, y2, z1, z2 = node1[0], node2[0], node1[1], node2[1], node1[2], node2[2]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            total_weight = 0
            for obstacle in obstacleList:
                total_weight += weightFinder(node1, node2, *obstacle)
            total_weight = total_weight - (len(obstacleList) - 1)*dist
            master_list.append([total_weight, node1, node2])
    print(master_list)
    return master_list
    ###2 parts
    #1. add the extra weight due to obstacle
    #2. add distance and just height difference b/w them
# if __name__ == "__main__":
#     print(weightFinder([2,0,0.5], [-1,1,0.5], 0, 1, 1, 0, 0, 1))
