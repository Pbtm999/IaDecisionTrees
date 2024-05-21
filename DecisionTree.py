from ID3 import ID3
from Node import Node
from Dataset import Dataset
import copy

class DecisionTree():

    def __init__(self, dataset, binning = False):
        self.initialDataset = dataset
        self.root = self.__generateNode(dataset)
        self.binning = binning

    def __generateNode(self, dataset, tabI=0, numRemovedColumns=0, value=None):
        attribute, values = ID3(dataset).bestAtributte
        node = Node(attribute, value, dataset.header[attribute])

        for key in values:
            isClass = False
            maxValue = float('-inf')
            maxkey = 'failed'
            maxkey2 = 'failed'
            for key2 in values[key]:
                if (key2 != "total"):
                    if (values[key][key2] == 1.0):
                        node.addNeighbour(Node(key2, key, None, True, values[key]["total"]))
                        isClass = True
                        break
                    elif (len(dataset.header) == 2):
                        if maxValue < values[key][key2] and key2 != "total":
                            maxValue = values[key][key2]
                            maxkey = key
                            maxkey2 = key2

            if (not isClass):
                if (len(dataset.header) == 2):
                    node.addNeighbour(Node(maxkey2, maxkey, None, True, int(values[maxkey]["total"]*values[maxkey][maxkey2])))
                else:
                    
                    datasetCopy = dataset.copy()
                    linestoRemove = []
                    for i in range(len(datasetCopy.array)):
                        if (datasetCopy.array[i][attribute] != key):
                            linestoRemove.append(i)

                    for x in sorted(linestoRemove, reverse=True):
                        datasetCopy.removeLine(x)

                    datasetCopy.removeColumn(attribute)

                    node.addNeighbour(self.__generateNode(datasetCopy, tabI+2, numRemovedColumns+1, key))

        return node

    def DFSPrint(self, tabI = 0, node = None):
        
        if (node == None):
            node = self.root
        
        print('\t'*tabI + '<'+node.label+'>')
        
        for currentNode in node.getNeighbours():

            if (currentNode.isClass):
                print(('\t'*(tabI+1))+currentNode.getValue()+': ' + currentNode.getAttribute() + ' (' + str(currentNode.counter) + ')')

            else:
                print(('\t'*(tabI+1))+currentNode.getValue()+':')
                self.DFSPrint(tabI+2, currentNode)

    def classifyMultipleExamples(self, path, file):

        dataset = Dataset().readCSV(path, file, True, False)
        for line in range(dataset.lines):
            classExmp = self.classifyExample(copy.deepcopy(dataset), line)
            if (classExmp == -1):
                print('Not Found!!')
            else:
                print('Line ' + str(line+1) + ' Class: ' + classExmp)
        return
    
    def classifyExample(self, dataset, line):

        actualNode = self.root
        value = dataset.array[line][actualNode.getAttribute()]

        while (actualNode.isClass != True):
            
            neighbours = actualNode.getNeighbours()
            
            found = False
            for node in (neighbours):
                if (self.binning == False):
                    if node.getValue() == value:
                        dataset.removeColumn(actualNode.getAttribute())
                        actualNode = node
                        if (actualNode.isClass != True): value = dataset.array[line][(actualNode.getAttribute())]
                        found = True
                        break
                else:
                    spliting = node.getValue().split('-')
                    if (spliting[0].replace(".", "", 1).isdigit() == True):
                        minVal = float(spliting[0])
                        maxVal = float(spliting[1])
                        value = float(value)
                        if value >= minVal and value <= maxVal:
                            dataset.removeColumn(actualNode.getAttribute())
                            actualNode = node
                            if (actualNode.isClass != True): value = dataset.array[line][(actualNode.getAttribute())]
                            found = True
                            break
                    else:
                        if node.getValue() == value:
                            dataset.removeColumn(actualNode.getAttribute())
                            actualNode = node
                            if (actualNode.isClass != True): value = dataset.array[line][(actualNode.getAttribute())]
                            found = True
                            break

            if (found == False): return -1
    
        return actualNode.getAttribute()