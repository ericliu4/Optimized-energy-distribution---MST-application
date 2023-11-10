from collections import defaultdict
def mapping(nodesList):
    keysToNodes = defaultdict(list)
    nodesToKeys = defaultdict(int)
    for index, (x,y,z) in enumerate(nodesList):
        keysToNodes[index] = [x,y,z]
        nodesToKeys[(x,y,z)] = index
    print('mapping complete')
    #print(nodesToKeys)
    #print(keysToNodes)
    return nodesToKeys, keysToNodes