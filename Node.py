class Node():

    def __init__(self, attribute, isClass = False):
        self.attribute = attribute
        self.isClass = isClass
        if (not isClass):
            self.values = []

    def addValue(self, value):
        self.values.append(value)
    
    def getValues(self):
        return self.values

        