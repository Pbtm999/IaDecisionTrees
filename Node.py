class Node():

    def __init__(self, attribute, value, label, isClass = False, counter = None):
        self.attribute = attribute
        self.isClass = isClass
        self.label = label
        self.value = value
        if (not isClass):
            self.neighbours = []
        else:
            self.counter = counter

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def getNeighbours(self):
        return self.neighbours
        
    def getAttribute(self):
        return self.attribute

    def getValue(self):
        return self.value