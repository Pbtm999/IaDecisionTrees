class Node():

    def __init__(self, attribute):
        self.attribute = attribute
        self.values = []

    def addValue(self, value):
        self.values.insert(value)
    
    def getValues(self):
        return self.values

        