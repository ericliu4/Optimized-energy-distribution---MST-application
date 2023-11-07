import pandas as pd
'''
file used to import data from all 3 CSV files
return list of lists back to simulate function

ObstacleLoader uses a riemann sum technique to 
add the difference in cost variable when going over 
high/low altitudes
'''
def nodesLoader(name):
    data = pd.read_csv(name)
    #print(data)
    lst = data[['XLocation', 'YLocation', 'ZLocation']].values.tolist()
    print(lst)
    return lst

def sourceLoader(name):
    data = pd.read_csv(name)
    #print(data)
    lst = data[['XLocation', 'YLocation', 'ZLocation']].values.tolist()
    print(lst)
    return lst

#add error checking function later (make sure the corners are correct) 
#aim to have an adjust function to be implemented later
def obstacleLoader(name):
    ##TopLeftX,TopLeftY,BottomRightX,BottomRightY,Height
    data = pd.read_csv(name)
    lst = data[['TopLeftX','TopLeftY', 'BottomRightX', 'BottomRightY', 'Height']].values.tolist()
    print(lst)
    return lst