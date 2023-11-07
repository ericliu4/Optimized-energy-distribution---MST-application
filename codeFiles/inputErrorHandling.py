def obstacleErrorHandling(lst):
    n = 0
    print('\n\nObstacle Error Handling\n\n')
    newList = []
    for TopLeftX,TopLeftY,BottomRightX,BottomRightY,Zstart,Height in lst:
        if (TopLeftX < BottomRightX and TopLeftY > BottomRightY and Zstart!=Height):
            print('Obstacle', n, ': normal')
            newList.append([TopLeftX,TopLeftY,BottomRightX,BottomRightY,Zstart,Height])
        else:
            if (TopLeftX == BottomRightX or TopLeftY == BottomRightY or Zstart == Height):
                print('Obstacle:', n, ': invalid values')
            else:
                newList.append([min(TopLeftX, BottomRightX), max(TopLeftY, BottomRightY), max(BottomRightX, TopLeftX), min(TopLeftY, BottomRightY),Zstart,Height])
                print('Obstacle:', n, ': input adjusted accordingly')
        n += 1
    return newList


#this part to be completely later after defining global max/min for the graph
def nodeHandling(lst):
    print('\n\nSourceNodeHandling\n\n')

    return lst