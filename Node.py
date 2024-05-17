class Node():

    def __init__(self, attribute, value, isClass = False):
        self.attribute = attribute
        self.isClass = isClass
        self.value = value
        if (not isClass):
            self.neighbours = []

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def getNeighbours(self):
        return self.neighbours
        
    def getAttribute(self):
        return self.attribute

    def getValue(self):
        return self.value

        